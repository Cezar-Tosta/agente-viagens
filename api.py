# api.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
from crewai import Crew
from travel_tasks import criar_tarefas_viagem
from weasyprint import HTML, CSS
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis locais (se existirem)

app = FastAPI(
    title="Assistente de Viagem com CrewAI",
    description="API para planejar viagens personalizadas usando agentes autônomos.",
    version="1.0.0"
)

# Rota para servir o index.html
@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", encoding="utf-8") as f:
        return HTMLResponse(f.read())

class TravelRequest(BaseModel):
    dias: int = 7
    orcamento_usd: int = 2000
    regiao_interesse: str = "internacional"

@app.post("/planejar_viagem", summary="Planeja uma viagem personalizada")
def planejar_viagem(request: TravelRequest):
    """
    Recebe parâmetros da viagem e retorna um relatório completo e sua avaliação.
    """
    try:
        tasks = criar_tarefas_viagem(
            dias=request.dias,
            orcamento=request.orcamento_usd,
            regiao=request.regiao_interesse
        )

        agents = list({task.agent for task in tasks})

        trip_crew = Crew(
            agents=agents,
            tasks=tasks,
            process="sequential",
            verbose=False
        )

        trip_crew.kickoff()

        relatorio = tasks[2].output
        avaliacao = tasks[3].output

        return {
            "status": "sucesso",
            "relatorio_viagem": str(relatorio),
            "avaliacao": str(avaliacao)
        }

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e)
        }

@app.post("/gerar_pdf", summary="Gera o relatório de viagem em PDF")
def gerar_pdf(request: TravelRequest):
    """
    Recebe os mesmos dados e retorna um PDF com o relatório.
    """
    try:
        tasks = criar_tarefas_viagem(
            dias=request.dias,
            orcamento=request.orcamento_usd,
            regiao=request.regiao_interesse
        )

        agents = list({task.agent for task in tasks})

        trip_crew = Crew(
            agents=agents,
            tasks=tasks,
            process="sequential",
            verbose=False
        )

        trip_crew.kickoff()

        relatorio = tasks[2].output

        # Formata o relatório em HTML com CSS
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Relatório de Viagem</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }}
                .section {{
                    margin: 20px 0;
                }}
            </style>
        </head>
        <body>
            <h1>Relatório de Viagem Personalizado</h1>
            <div class="section">
                <h2>Itinerário para {request.dias} dias com orçamento de US${request.orcamento_usd}</h2>
                <pre>{relatorio}</pre>
            </div>
            <p><small>Gerado por Assistente de Viagem Inteligente com CrewAI</small></p>
        </body>
        </html>
        """

        # Gera o PDF
        html = HTML(string=html_content)
        css = CSS(string="""
            @page {{
                margin: 1cm;
            }}
            pre {{
                white-space: pre-wrap;
            }}
        """)
        pdf_bytes = html.write_pdf(stylesheets=[css])

        return StreamingResponse(
            BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=relatorio_viagem_{request.dias}dias.pdf"
            }
        )

    except Exception as e:
        return {
            "status": "erro",
            "mensagem": str(e)
        }
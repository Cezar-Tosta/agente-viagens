from crewai.tools import BaseTool
from sqlalchemy import create_engine, text
import os

class DatabaseReaderTool(BaseTool):
    name: str = "Leitor de Banco de Dados"
    description: str = (
        "Conecta a um banco de dados e executa consultas SQL para obter informações. "
        "Use consultas SELECT para ler dados. Exemplo: 'SELECT * FROM hotels WHERE city = 'Paris'"
    )

    def _run(self, query: str) -> str:
        # Obter string de conexão do .env
        database_url = os.getenv("DATABASE_URL")

        if not database_url:
            return "Erro: DATABASE_URL não está definida no .env"

        try:
            # Conectar ao banco
            engine = create_engine(database_url)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()

                if not rows:
                    return "Nenhum resultado encontrado."

                # Converter resultados para string
                columns = list(result.keys())
                output = [", ".join(columns)]
                for row in rows:
                    output.append(", ".join(str(cell) for cell in row))

                return "\n".join(output)

        except Exception as e:
            return f"Erro na consulta: {str(e)}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Método assíncrono não suportado.")
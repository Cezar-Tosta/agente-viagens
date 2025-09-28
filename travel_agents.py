from crewai import Agent
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from tools.currency_converter_tool import CurrencyConverterTool
from tools.drive_reader_tool import DriveReaderTool
from tools.database_reader_tool import DatabaseReaderTool

load_dotenv()  # Carrega as variáveis do .env

# Ferramentas
search_tool = SerperDevTool()
currency_tool = CurrencyConverterTool()
# Ferramenta para ler arquivos do Drive
drive_tool = DriveReaderTool()
# Ferramenta para ler banco de dados
db_tool = DatabaseReaderTool()

# Agentes
pesquisador_viagem = Agent(
    role="Pesquisador de Viagens",
    goal="Pesquisar e recomendar destinos com base em orçamento, duração e interesses do usuário",
    backstory="Você é um especialista global em turismo com acesso a dados em tempo real sobre voos, hotéis e atrações.",
    tools=[search_tool],
    verbose=True
)

planejador_roteiros = Agent(
    role="Planejador de Roteiros",
    goal="Criar itinerários diários detalhados e realistas para viagens",
    backstory="Você é um planejador de viagens profissional com expertise em logística, horários e experiências locais autênticas.",
    verbose=True
)

escritor_viagens = Agent(
    role="Escritor de Viagens",
    goal="Transformar planos de viagens em relatórios cativantes e fáceis de seguir",
    backstory="Você é um escritor de viagens premiado, conhecido por guiar leitores com clareza, entusiasmo e dicas práticas.",
    tools=[currency_tool],
    verbose=True
)

avaliador_viagem = Agent(
    role="Avaliador de Qualidade de Viagens",
    goal="Verificar se o relatório de viagem atende aos critérios de qualidade",
    backstory="Você é um editor-chefe com olho clínico para detalhes essenciais.",
    verbose=True
)

pesquisador_dados = Agent(
    role="Pesquisador de Dados de Viagem",
    goal="Buscar informações relevantes em documentos do Google Drive para enriquecer o relatório de viagem",
    backstory="Você tem acesso a uma pasta do Google Drive com avaliações, dicas e informações de viagens anteriores.",
    tools=[drive_tool],
    verbose=True
)

pesquisador_db = Agent(
    role="Pesquisador de Banco de Dados",
    goal="Consultar o banco de dados para encontrar informações atualizadas",
    backstory="Você tem acesso a um banco de dados com informações de interesse para os relatórios de viagens.",
    tools=[db_tool],
    verbose=True
)

# Só imprime os agentes se este arquivo for executado diretamente
if __name__ == "__main__":
    print(f"""Agentes criados com sucesso:
    - {pesquisador_viagem.role};
    - {planejador_roteiros.role}; 
    - {escritor_viagens.role};
    - {avaliador_viagem.role};
    - {pesquisador_dados.role}; e
    - {pesquisador_db.role}""")
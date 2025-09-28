from crewai import Agent
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from tools.currency_converter_tool import CurrencyConverterTool

load_dotenv()  # Carrega as variáveis do .env

# Ferramentas
search_tool = SerperDevTool()
currency_tool = CurrencyConverterTool()

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

# Só imprime os agentes se este arquivo for executado diretamente
if __name__ == "__main__":
    print(f"""Agentes criados com sucesso:
    - {pesquisador_viagem.role};
    - {planejador_roteiros.role}; 
    - {escritor_viagens.role}; e
    - {avaliador_viagem.role}.""")
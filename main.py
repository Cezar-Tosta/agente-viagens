from crewai import Crew
from travel_agents import pesquisador_viagem, planejador_roteiros, escritor_viagens, avaliador_viagem, pesquisador_dados, pesquisador_db
from travel_tasks import pesquisar_destinos, planejar_itinerario, escrever_relatorio, avaliar_relatorio, pesquisar_dados_drive, pesquisar_dados_db

if __name__ == "__main__":
    trip_crew = Crew(
        agents=[pesquisador_viagem, planejador_roteiros, escritor_viagens, avaliador_viagem, pesquisador_dados, pesquisador_db],
        tasks=[pesquisar_destinos, planejar_itinerario, escrever_relatorio, avaliar_relatorio, pesquisar_dados_drive, pesquisar_dados_db],
        process='sequential',
        verbose=True
    )

    # Executa a Crew
    final_result = trip_crew.kickoff()

    # Acessa os resultados individuais
    relatorio_viagem = escrever_relatorio.output  # ← resultado do 3º agente
    avaliacao = avaliar_relatorio.output          # ← resultado do 4º agente (igual a final_result)
    dicas_finais = pesquisar_dados_drive.output   # ← resultado do 5º agente
    banco_dados = pesquisar_dados_db.output   # ← resultado do 6º agente

    print("\n" + "="*50)
    print("📄 RELATÓRIO DE VIAGEM (3º agente)")
    print("="*50)
    print(relatorio_viagem)

    print("\n" + "="*50)
    print("🔍 AVALIAÇÃO DE QUALIDADE (4º agente)")
    print("="*50)
    print(avaliacao)

    print("\n" + "="*50)
    print("🔍 DICAS FINAIS com base no DRIVE (5º agente)")
    print("="*50)
    print(dicas_finais)

    print("\n" + "="*50)
    print("🔍 DICAS FINAIS com base no BANCO DE DADOS (6º agente)")
    print("="*50)
    print(banco_dados)
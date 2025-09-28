from crewai import Crew
from travel_agents import pesquisador_viagem, planejador_roteiros, escritor_viagens, avaliador_viagem
from travel_tasks import pesquisar_destinos, planejar_itinerario, escrever_relatorio, avaliar_relatorio

if __name__ == "__main__":
    trip_crew = Crew(
        agents=[pesquisador_viagem, planejador_roteiros, escritor_viagens, avaliador_viagem],
        tasks=[pesquisar_destinos, planejar_itinerario, escrever_relatorio, avaliar_relatorio],
        process='sequential',
        verbose=True
    )

    # Executa a Crew
    final_result = trip_crew.kickoff()

    # Acessa os resultados individuais
    relatorio_viagem = escrever_relatorio.output  # ← resultado do 3º agente
    avaliacao = avaliar_relatorio.output          # ← resultado do 4º agente (igual a final_result)

    print("\n" + "="*50)
    print("📄 RELATÓRIO DE VIAGEM (3º agente)")
    print("="*50)
    print(relatorio_viagem)

    print("\n" + "="*50)
    print("🔍 AVALIAÇÃO DE QUALIDADE (4º agente)")
    print("="*50)
    print(avaliacao)
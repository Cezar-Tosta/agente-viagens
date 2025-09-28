from crewai import Task
from travel_agents import pesquisador_viagem, planejador_roteiros, escritor_viagens, avaliador_viagem

# =============== TAREFAS ESTÁTICAS (para testes locais) ===============
pesquisar_destinos = Task(
    description=(
        "Pesquise 3 destinos internacionais acessíveis para uma viagem de 7 dias "
        "com orçamento de até US$2000, incluindo voos e hospedagem. "
        "Use a ferramenta de busca na internet para obter dados atualizados."
    ),
    expected_output=(
        "Lista com: nome do destino, custo total estimado (voos + hotel), "
        "melhores meses para visitar e 3 atrações imperdíveis."
    ),
    agent=pesquisador_viagem
)

planejar_itinerario = Task(
    description=(
        "Com base na lista de destinos e custos gerada pelo Pesquisador de Viagens, "
        "selecione o destino mais recomendado e crie um itinerário detalhado de 7 dias. "
        "Inclua atividades diárias, horários sugeridos e tempo de deslocamento."
    ),
    expected_output=(
        "Itinerário numerado por dia, com horários, atividades, locais e dicas práticas."
    ),
    agent=planejador_roteiros
)

escrever_relatorio = Task(
    description=(
        "Com base no itinerário criado pelo Planejador de Roteiros, "
        "escreva um relatório de viagem envolvente e pronto para uso. "
        "Inclua introdução, dicas gerais, resumo do roteiro e conclusão inspiradora."
        "Considere cada um dos dias descritos pelo Planejador de Roteiros e escreva sobre cada um separadamente."
    ),
    expected_output=(
        "Relatório em linguagem natural, com título, parágrafos bem estruturados "
        "e tom acolhedor."
    ),
    agent=escritor_viagens
)

avaliar_relatorio = Task(
    description=(
        "Verifique se o relatório final contém: "
        "(1) O destino com custos, "
        "(2) Itinerário de 7 dias detalhado, "
        "(3) Tom envolvente. "
        "Se faltar algo, liste o que está ausente."
    ),
    expected_output="Lista do que está OK e do que está faltando.",
    agent=avaliador_viagem
)

print("""\nTarefas criadas com sucesso:
    - Pesquisar Destinos;
    - Planejar Itinerário;
    - Escrever Relatório; e
    - Avaliar Relatório.""")

# =============== FUNÇÃO PARA TAREFAS DINÂMICAS (para API) ===============
def criar_tarefas_viagem(dias: int = 7, orcamento: int = 2000, regiao: str = "internacional"):
    """Gera tarefas personalizadas para uso em APIs ou interfaces interativas."""
    t1 = Task(
        description=(
            f"Pesquise 3 destinos {regiao} acessíveis para uma viagem de {dias} dias "
            f"com orçamento de até US${orcamento}, incluindo voos e hospedagem."
        ),
        expected_output=(
            "Lista com: nome do destino, custo total estimado, melhores meses e 3 atrações."
        ),
        agent=pesquisador_viagem
    )

    t2 = Task(
        description=(
            f"Com base nos destinos sugeridos, crie um itinerário detalhado de {dias} dias "
            "para o destino mais recomendado."
        ),
        expected_output="Itinerário numerado por dia com horários e atividades.",
        agent=planejador_roteiros
    )

    t3 = Task(
        description="Escreva um relatório de viagem envolvente com base no itinerário.",
        expected_output="Relatório em linguagem natural com título e conclusão.",
        agent=escritor_viagens
    )

    t4 = Task(
        description=(
            "Verifique se o relatório contém: destino com custos, itinerário de "
            f"{dias} dias e tom envolvente. Liste o que está faltando."
        ),
        expected_output="Lista do que está OK e do que está ausente.",
        agent=avaliador_viagem
    )

    return [t1, t2, t3, t4]
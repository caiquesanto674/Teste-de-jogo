from src.economy import Economia, BaseMilitar
from src.agent import AgentePPO
from src.units import UnidadeMilitar, UnidadeSuporte

def main():
    """Função principal para simular o jogo."""
    # Configuração inicial
    economia = Economia()
    base = BaseMilitar()
    agente_comandante = AgentePPO()
    agente_inimigo = AgentePPO()

    comandante = UnidadeMilitar("Comandante", 20, 100, agente_comandante)
    suporte = UnidadeSuporte("Suporte", 5, 50, AgentePPO())
    inimigo = UnidadeMilitar("Inimigo", 30, 100, agente_inimigo)

    print("--- Início da Simulação ---")
    print(f"Recursos Iniciais da Base: {base.recursos}")
    print(f"Moral Inicial da Base: {base.moral}")
    print("-" * 20)

    # Turno 1: Ações da Base e do Comandante
    print("--- Turno 1 ---")
    print(economia.gerar(base))
    print(base.aplicar_impacto(10))
    print(f"Recursos Atuais da Base: {base.recursos}")
    print(f"Moral Atual da Base: {base.moral}")
    print("-" * 20)

    # Ação do Comandante
    print(comandante.acao(inimigo, suporte, base))
    print(f"HP Inimigo: {inimigo.hp}/{inimigo.max_hp}")
    print(f"Éter restante: {base.recursos['Éter']}")
    print("-" * 20)

    # Ação do Inimigo (Contra-ataque)
    print(inimigo.acao(comandante, None, base))
    print(f"HP Comandante: {comandante.hp}/{comandante.max_hp}")
    print("-" * 20)

    # Ação da Unidade de Suporte
    print(suporte.acao(comandante, None))
    print(f"HP Comandante após cura: {comandante.hp}/{comandante.max_hp}")
    print("-" * 20)

    print("--- Fim da Simulação ---")


if __name__ == "__main__":
    main()
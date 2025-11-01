from .game.base_militar import BaseMilitar
from .game.unidade_militar import Soldado, Oficial

def main():
    """
    Função principal para executar a simulação do jogo.
    """
    # Cria a base militar a partir do config
    base = BaseMilitar()

    # Adiciona unidades à base
    base.adicionar_unidade(Soldado("Carlos", "Cabo"))
    base.adicionar_unidade(Oficial("Ana", "Major"))

    # Simula algumas ações
    base.economia.produzir("comida", 35)
    base.registrar_evento("Patrulha iniciou missão de reconhecimento.")

    # Exibe o status final e o log de eventos
    print("==== RESUMO DA BASE ====")
    print(base.status_base())
    print("\nLog de eventos:", base.evento_log)

if __name__ == "__main__":
    main()

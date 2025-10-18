from src.core import MilitaryBase
from src.economy import Technology, Economy
from src.ai import AIProtocol
from src.entities import Character

# ==================== FUNÇÃO PRINCIPAL ====================
from src.core import Resource

def main():
    # Criação da base e módulos
    base = MilitaryBase()
    technology = Technology()
    available_resources = [Resource("Éter", 50.0)]
    economy = Economy(base, technology)
    ai_protocol = AIProtocol(economy, available_resources)

    # Protagonista e Agentes OP
    protagonist = Character("Caíque (Apolo)", volicao_level=99)
    base.add_soldier(protagonist)
    base.add_soldier(Character("Basara (Aliada Harem)", volicao_level=40))

    # Exibição do status inicial
    base.display_status()

    # 1. Execução da análise automática da AI (AI Tycoon)
    ai_protocol.analyze_and_execute()

    # 2. Upgrade tecnológico (Ação Tycoon)
    economy.upgrade_technology(200)

    # 3. Confirmação de ação pelo Protagonista (Poder Psicológico / Volição)
    protagonist.confirm_action("Ciclo de Aquisição de Éter e Otimização de Força Bélica concluído.")

    # Exibição do status final
    base.display_status()

if __name__ == "__main__":
    main()
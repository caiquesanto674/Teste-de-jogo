import time
from src.simulation import MilitaryBase

# ==================== EXECUÇÃO FINAL ====================
if __name__ == "__main__":
    base = MilitaryBase("Baluarte Solaris / CORE NEXUS")
    # Protagonista
    base.add_character("Caíque (Apolo)", "Comandante Supremo (Protagonista)")
    # Aliados
    base.add_character("Basara", "Aliada (Harem/Chefe Tática)")
    base.add_character("VMZoficial", "Chefe de Força Bélica")
    # Inimigo
    base.add_character("Enygma", "Inimigo (Líder de Facção)")

    # Simulação de 3 ciclos
    for c in range(3):
        base.cycle()
        time.sleep(0.5)
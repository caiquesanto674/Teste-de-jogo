import random
from datetime import datetime
from typing import List
from src.services import StorageService
from src.economy import Economy
from src.protocols import AIProtocol
from src.entities import Character
from src.metrics import MetricXValidator

# ==================== MÓDULO 7: CORE NEXUS (CONTROLADOR PRINCIPAL) ====================
class MilitaryBase:
    """
    A classe principal do jogo, que representa a base militar e gerencia o
    ciclo de simulação.
    """
    def __init__(self, name: str):
        """
        Inicializa a base militar e todos os seus submódulos.

        Args:
            name: O nome da base militar.
        """
        self.name = name
        self.storage = StorageService()
        self.economy = Economy()
        self.ai = AIProtocol()
        self.metrics = MetricXValidator()
        self.characters: List[Character] = []
        self.game_status = {"volicao_audacia": 0.98, "defense": 100}

    def add_character(self, name: str, role: str):
        """
        Adiciona um novo personagem à simulação e o salva no armazenamento.

        Args:
            name: O nome do personagem.
            role: O papel do personagem.
        """
        char = Character(name, role)
        self.characters.append(char)
        self.storage.save(f"char_{char.id}", char.to_dict())
        print(f"\n[CONTEÚDO NOVO]: {name} ({role}) - Nível de Força: {char.powers.force_level}.")

    def add_random_character(self):
        """
        Adiciona aleatoriamente um novo personagem à simulação, com base em uma
        chance predefinida.
        """
        if random.random() > 0.8:
            new_role = random.choice(["Aliada (Harem)", "Inimigo (Elite)"])
            self.add_character(f"NPC_AURORA_{random.randint(100,999)}", new_role)

    def cycle(self):
        """
        Executa um único ciclo de simulação, que inclui a atualização da economia,
        a evolução da IA, a validação de métricas e a exibição de logs.
        """
        print(f"\n==================== [CICLO {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ====================")

        # 1. ECONOMIA E TECNOLOGIA
        self.economy.update_market()
        if self.economy.gold > 800 and random.random() < 0.3:
            if self.economy.upgrade_technology():
                self.ai.log.append(f"{datetime.now().strftime('%H:%M:%S')}: AUTO_UPGRADE_TRIGGER - Tech Level: {self.economy.technology:.2f}.")

        # 2. IA, CÓDIGO E NARRATIVA
        self.ai.evolve_and_verify()
        self.add_random_character()

        # Atualização da Volição/Audácia
        self.game_status["volicao_audacia"] *= random.uniform(0.95, 1.05)
        self.game_status["volicao_audacia"] = max(0.1, min(self.game_status["volicao_audacia"], 1.0))


        # 3. MÉTRICA X (DESEMPENHO AVANÇADO)
        impact, latency, data_share = self.metrics.validate(self.game_status["volicao_audacia"])

        # 4. SINCRONIZAÇÃO E LOG DE ATITUDE (Comportamento em Código)
        self.storage.sync()
        if self.characters:
            print(f"\n[LOG DE ATITUDE - PROTAGONISTA/ALIADOS]")
            for char in self.characters:
                 print(f" > {char.get_confirmation_phrase()}")

        # 5. EXIBIÇÃO DA MÉTRICA X FINAL
        print(f"\n--- [MÉTRICA X: DESEMPENHO AVANÇADO] ---")
        print(f"Impacto Estratégico (Felicidade): {impact:.3f} (Volição: {self.game_status['volicao_audacia']:.2f})")
        print(f"Latência de Comando (Pato, ms): {latency:.2f} ms (Otimizado por Tech)")
        print(f"Animac 20 (Dados/Compartilhamento): {'ATIVO' if data_share else 'INATIVO'}")
        print(f"Nível Tech (AI V{self.ai.version:.2f}): {self.economy.technology:.2f} | Ouro: {self.economy.gold:.2f}")

        # Exibição de logs
        print("\n[LOGS DO SISTEMA]")
        for log_entry in self.storage.log:
            print(f" > {log_entry}")
        for log_entry in self.ai.log:
            print(f" > {log_entry}")

        print("=======================================================================")
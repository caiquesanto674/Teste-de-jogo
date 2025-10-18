import random
import time
from datetime import datetime
from typing import List

from .core.auth_manager import AuthManager
from .core.character_system import Character
from .core.economy_system import Economy
from .core.narrative_ai import AIProtocol
from .core.metrics_system import MetricXValidator
from .integrations.storage_service import StorageService

class MilitaryBase:
    """
    [PT] Núcleo do jogo: centraliza economia, IA, personagens, métricas.
    [EN] Main game core: centralizes economy, AI, characters, metrics.
    """

    def __init__(self, name, auth_manager, provider='Azure-Google'):
        self.name = name
        self.storage = StorageService(provider)
        self.economy = Economy()
        self.auth = auth_manager
        self.ai_stack = [
            AIProtocol("Defense/Tactics"),
            AIProtocol("Market AI")
        ]
        self.metrics = MetricXValidator()
        self.characters: List[Character] = []
        self.game_status = {"defense": 5, "effectiveness": 0.95}

    def add_character(self, name, role):
        char = Character(name, role)
        self.characters.append(char)
        self.auth.login(char)
        self.storage.save(f"char_{char.id}", vars(char))
        print(f"Character '{name}' ({role}) added to base.")

    def cycle(self):
        print(
            f"\n--- [CYCLE/CICLO {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ---"
        )
        # Economia/Mercado
        self.economy.update_market()

        # Admin Bonus
        if self.auth.logged_in_user and self.auth.is_admin(self.auth.logged_in_user):
            self.economy.gold += 100
            self.game_status["defense"] += 1
            print("[ADMIN] Monarca bonus applied: +100 Gold, +1 Defense.")

        # IA/Analise Contextual
        context = {"economy": self.economy, "characters": self.characters}
        for ai in self.ai_stack:
            ai.analyze_context(context)
            ai.auto_learn()

        # Métrica X
        impact, latency, morale = self.metrics.validate(
            self.game_status["effectiveness"]
        )
        # Adiciona personagem aleatório
        if random.random() > 0.88:
            self.add_character(
                f"NPC_{random.randint(100,999)}",
                random.choice(["Aliado", "Inimigo"]),
            )
            for ai in self.ai_stack:
                 if ai.name == "Defense/Tactics":
                    ai.log.append(
                        f"{datetime.now()}: Novo personagem/narrativa inserido."
                    )
        # Sincronização Cloud
        self.storage.sync()
        # Frase confirmação comportamental
        if self.characters:
            print(
                f"[FEEDBACK] {random.choice(self.characters).get_confirmation_phrase()}"
            )
        # Métricas
        print(f"\n--- [MÉTRICA X: DESEMPENHO/PERFORMANCE] ---")
        print(
            f"Impacto Estratégico/Impact: {impact:.3f} | Latência/Latency: {latency:.2f} ms | Moral/Morale: {'ALTA/HIGH' if morale else 'BAIXA/LOW'}"
        )
        print(
            f"Tech Level: {self.economy.technology:.2f} | Preço Metal/Metal Price: {self.economy.prices['metal']:.2f}"
        )
        # Print AI logs
        for ai in self.ai_stack:
             print(
                f"IA {ai.name} v{ai.version:.2f} | Último log/Last log: {ai.log[-1] if ai.log else 'N/A'}"
            )

def main():
    auth_manager = AuthManager()
    # Admin registration/authentication
    auth_manager.register("Caíque", "password123") # In a real app, this would be secure

    base = MilitaryBase("Aurora Nexus / Baluarte Solaris", auth_manager, "Azure-Google")
    base.add_character("Caíque", "Comandante Supremo/Supreme Commander")
    base.add_character("Sydra", "Chefe Defesa/Defense Chief")
    # Simulação de 3 ciclos/3 cycles
    for c in range(3):
        base.cycle()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
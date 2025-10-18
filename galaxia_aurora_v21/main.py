import random
import time
from datetime import datetime
from typing import List, Dict, Any

from .core.auth_manager import AuthManager
from .core.character_system import Character
from .core.economy_system import Economy
from .core.narrative_ai import AIProtocol
from .core.metrics_system import MetricXValidator
from .core.tactical_ai import PPOAgent, ActionType
from .integrations.storage_service import StorageService
from .integrations.secure_backup import SecureBackup

class GameEngine:
    """
    [PT] Núcleo do jogo: centraliza economia, IA, personagens, métricas.
    [EN] Main game core: centralizes economy, AI, characters, metrics.
    """

    def __init__(self, name, auth_manager, secure_backup, storage_service):
        self.name = name
        self.storage = storage_service
        self.economy = Economy()
        self.auth = auth_manager
        self.secure_backup = secure_backup
        self.narrative_ai_stack = [
            AIProtocol("Defense/Tactics"),
            AIProtocol("Market AI")
        ]
        self.tactical_ai = PPOAgent()
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
        # Economy/Market
        self.economy.update_market()

        # Admin Bonus
        if self.auth.logged_in_user and self.auth.is_admin(self.auth.logged_in_user):
            self.economy.gold += 100
            self.game_status["defense"] += 1
            print("[ADMIN] Monarca bonus applied: +100 Gold, +1 Defense.")

        # Narrative AI Analysis
        context = {"economy": self.economy, "characters": self.characters}
        for ai in self.narrative_ai_stack:
            ai.analyze_context(context)
            ai.auto_learn()

        # Tactical AI Combat Phase
        if any(char.role == "Inimigo" for char in self.characters):
            tactical_context = {"health": 100, "support_available": True} # Simplified context
            action = self.tactical_ai.decide_action(tactical_context)
            print(f"[TACTICAL] Commander decides to {action.name}.")
            # In a real game, this action would have consequences.
            self.tactical_ai.learn(action, random.uniform(-0.1, 0.1)) # Simulate reward

        # Metric X
        impact, latency, morale = self.metrics.validate(
            self.game_status["effectiveness"]
        )
        # Add random character
        if random.random() > 0.88:
            self.add_character(
                f"NPC_{random.randint(100,999)}",
                random.choice(["Aliado", "Inimigo"]),
            )

        # Cloud Sync and Backup
        self.storage.sync()
        backup_data = {"gold": self.economy.gold, "tech": self.economy.technology, "defense": self.game_status['defense']}
        self.secure_backup.backup(f"backup_{self.name.replace(' ', '_')}_{datetime.now().strftime('%H%M%S')}", backup_data)

        # Behavioral confirmation phrase
        if self.characters:
            print(
                f"[FEEDBACK] {random.choice(self.characters).get_confirmation_phrase()}"
            )
        # Metrics
        print(f"\n--- [MÉTRICA X: DESEMPENHO/PERFORMANCE] ---")
        print(
            f"Impacto Estratégico/Impact: {impact:.3f} | Latência/Latency: {latency:.2f} ms | Moral/Morale: {'ALTA/HIGH' if morale else 'BAIXA/LOW'}"
        )
        print(
            f"Tech Level: {self.economy.technology:.2f} | Preço Metal/Metal Price: {self.economy.prices['metal']:.2f}"
        )
        # Print AI logs
        for ai in self.narrative_ai_stack:
             print(
                f"IA {ai.name} v{ai.version:.2f} | Último log/Last log: {ai.log[-1] if ai.log else 'N/A'}"
            )

def main():
    auth_manager = AuthManager()
    storage = StorageService("Azure-Google")
    secure_backup = SecureBackup(storage)

    # Admin registration/authentication
    auth_manager.register("Caíque de Jesus Santos", "password123") # In a real app, this would be secure

    base = GameEngine("Aurora Nexus / Baluarte Solaris", auth_manager, secure_backup, storage)
    base.add_character("Caíque de Jesus Santos", "Monarca")
    base.add_character("Sydra", "Chefe Defesa/Defense Chief")
    # Simulation of 3 cycles
    for c in range(3):
        base.cycle()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
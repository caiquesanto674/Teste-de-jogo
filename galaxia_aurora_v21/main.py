import time
import random
from .core.character_system import Character
from .core.economy_system import Economy
from .core.tactical_ai import PPOAgent
from .core.narrative_ai import AIProtocol
from .core.auth_manager import AuthManager
from .integrations.cloud_storage import CloudStorage
from .integrations.secure_backup import SecureBackup

class GameEngine:
    def __init__(self, storage_provider: str):
        self.auth = AuthManager()
        self.economy = Economy()
        self.ai_protocol = AIProtocol()
        self.cloud_storage = CloudStorage(storage_provider)
        self.secure_backup = SecureBackup(self.cloud_storage)
        self.characters: dict[str, Character] = {}
        self.active_character: Character = None

    def add_character(self, name: str, role: str):
        char = Character(name, role)
        self.characters[char.id] = char
        print(f"Character '{name}' ({role}) created with ID: {char.id}")
        if self.active_character is None:
            self.active_character = char
            self.auth.login(char)
        return char

    def cycle(self):
        print(f"\n--- Cycle for {self.active_character.name} ---")

        # 1. Economy Update
        self.economy.update_market()
        print(f"Market updated. Metal Price: {self.economy.resources['metal']:.2f}, Gold: {self.economy.gold:.2f}")

        # 2. AI Protocol Analysis
        context = {"threat": random.choice([True, False]), "market_crash": random.random() < 0.1}
        self.ai_protocol.analyze_context(context)
        self.ai_protocol.show_log()

        # 3. Secure Backup
        if random.random() > 0.7: # Randomly decide to backup
            game_state = {"gold": self.economy.gold, "character_health": self.active_character.health}
            self.secure_backup.create_backup(game_state, f"backup_{self.active_character.name}_{int(time.time())}")
            self.cloud_storage.sync()

        # 4. Admin Privileges Check
        privileges = self.auth.get_user_privileges()
        if privileges.get("has_god_mode"):
            print("[ADMIN] God Mode Active: Health set to 999.")
            self.active_character.health = 999

def main():
    engine = GameEngine('Azure')

    # Adding initial characters
    admin_char = engine.add_character("Caíque de Jesus Santos", "Supreme Commander")
    engine.add_character("Sydra", "Defense Chief")

    # Simulating 3 game cycles
    for cycle in range(3):
        print(f"\n>>> Cycle {cycle + 1} <<<")
        engine.cycle()
        time.sleep(1)

if __name__ == "__main__":
    main()
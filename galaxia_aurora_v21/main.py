import random
import time
from datetime import datetime
from typing import List

from .core.auth_manager import AuthManager
from .core.character_system import Character
from .core.economy_system import Economy
from .core.narrative_ai import AIModule
from .core.crypto_chat import CryptoChat
from .integrations.cloud_storage import CloudStorage
from .integrations.secure_backup import SecureBackup

class ChatLog:
    def __init__(self):
        self.log: List[Dict[str, str]] = []

    def send(self, user: str, msg: str):
        record = {"user": user, "msg": msg, "time": datetime.now().strftime("%d/%m/%Y %H:%M")}
        self.log.append(record)

    def view_log(self, last: int = 5):
        print("\n---- Last messages/actions ----")
        for item in self.log[-last:]:
            print(f"[{item['time']}] {item['user']}: {item['msg']}")

class MilitaryBase:
    """Game command center, simulates a complete operational cycle."""
    def __init__(self, name: str, auth: AuthManager, chat: CryptoChat, econ: Economy, backup: SecureBackup, ai_stack: List[AIModule], chat_log: ChatLog):
        self.name = name
        self.auth = auth
        self.chat = chat
        self.econ = econ
        self.backup = backup
        self.ai_stack = ai_stack
        self.chat_log = chat_log
        self.characters: List[Character] = []
        self.defense_level = 3

    def add_character(self, name: str, role: str) -> Character:
        new_char = Character(name, role)
        self.characters.append(new_char)
        self.auth.login(new_char) # Log in character on creation
        phrase = new_char.speak()
        self.chat_log.send(new_char.name, f"New character activated: {phrase}")
        return new_char

    def cycle(self):
        print(f"\n==== Operation cycle: {datetime.now().strftime('%d/%m/%Y %H:%M')} ====")
        self.econ.update_market()

        if self.auth.is_admin(self.auth.logged_in_user):
            self.econ.balance += 100
            self.defense_level += 1
            self.chat_log.send("SYSTEM", "Monarca admin bonus applied: +100 Gold, +1 Defense")

        context = {"economy": self.econ, "characters": self.characters}
        ai_responses = [ia.analyze(context) for ia in self.ai_stack]

        for ia in self.ai_stack:
            ia.auto_learn()

        for p in self.characters:
            phrase = p.speak()
            print(phrase)
            self.chat_log.send(p.name, phrase)

        backup_data = str({"econ_balance": self.econ.balance, "defense": self.defense_level})
        self.backup.backup(f"backup_{self.name}_{datetime.now().strftime('%H%M%S')}", backup_data)
        print(f"Current defense: {self.defense_level} | Balance: {self.econ.balance:.2f} | Tech: {self.econ.tech_level:.2f}")
        self.chat_log.view_log()
        print("----------- End of cycle -----------\n")

def main():
    auth_manager = AuthManager()
    economy_system = Economy()
    crypto_chat = CryptoChat()
    secure_backup = SecureBackup(CloudStorage('Azure'))
    chat_log = ChatLog()
    ai_modules = [
        AIModule("Defense/Tactics"),
        AIModule("Market AI"),
        AIModule("AntiSpam/Messaging")
    ]

    auth_manager.register("admin", "strong_password")
    mfa_code = auth_manager.users["admin"]["mfa_code"]
    print("Login successful:", auth_manager.authenticate("admin", "strong_password", mfa_code))

    base = MilitaryBase("Aurora Nexus", auth_manager, crypto_chat, economy_system, secure_backup, ai_modules, chat_log)
    base.add_character("Caíque de Jesus Santos", "Monarca")
    base.add_character("Sydra", "Head of Defense")
    base.add_character("Pyra", "AI Technician")

    for i in range(3):
        print(f"\n--- CYCLE {i+1} ---")
        base.cycle()
        time.sleep(0.3)

    # Example of encrypted message
    encrypted_message = crypto_chat.send("Caleb", "Pyra", "Review perimeter, reinforce smart AI defense.")
    crypto_chat.receive(encrypted_message)

if __name__ == "__main__":
    main()
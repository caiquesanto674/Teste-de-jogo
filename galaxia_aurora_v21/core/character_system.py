import uuid
import random

class Character:
    """Playable or NPC character with confirmation phrases."""
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.level = 1
        self.confirm_code = f"CONFIRM_{role.upper()}_{random.randint(100, 999)}"
        self.phrases = [
            f"{self.role} '{self.name}': Base is under control. {self.confirm_code}",
            f"{self.role} '{self.name}': Sector safe, monitoring.",
            f"{self.role} '{self.name}': AI command received and coded.",
            f"{self.role} '{self.name}': Level {self.level}, ready for action."
        ]
    def speak(self) -> str:
        return random.choice(self.phrases)
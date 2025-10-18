import uuid
import random

class Character:
    """
    [PT] Personagem/NPC com frases de confirmação dinâmicas.
    [EN] Character/NPC with dynamic confirmation phrases.
    """

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.id = uuid.uuid4().hex
        self.level = 1

    def get_confirmation_phrase(self) -> str:
        phrases = [
            f"{self.role} '{self.name}': Base segura, patrulha verde. // Base secure, patrol green.",
            f"{self.role} '{self.name}': Prontidão de combate confirmada. // Combat readiness confirmed.",
            f"{self.role} '{self.name}': Comando IA verificado. // AI command verified.",
            f"{self.role} '{self.name}': Nível {self.level}, operação pronta. // Level {self.level}, operation ready.",
        ]
        return random.choice(phrases)
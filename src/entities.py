import uuid
import random
from src.protocols import PowerProtocol

# ==================== MÓDULO 5: PERSONAGENS E CONFIRMAÇÃO ====================
class Character:
    """
    Representa um personagem no jogo, com um nome, papel, ID único e um
    conjunto de poderes definidos pelo PowerProtocol.
    """
    def __init__(self, name: str, role: str):
        """
        Inicializa um novo personagem.

        Args:
            name: O nome do personagem.
            role: O papel do personagem.
        """
        self.name = name
        self.role = role
        self.id = uuid.uuid4().hex
        self.powers = PowerProtocol(role)

    def to_dict(self):
        """
        Converte o objeto Character em um dicionário que pode ser serializado.

        Returns:
            Um dicionário representando o personagem.
        """
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "powers": {
                "role": self.powers.role,
                "force_level": self.powers.force_level,
                "abilities": self.powers.abilities,
            },
        }

    def get_confirmation_phrase(self) -> str:
        """
        Gera uma frase de confirmação de comportamento com base nas habilidades
        e no papel do personagem.

        Returns:
            Uma frase de confirmação de comportamento.
        """
        phrases = [
            f"PROTOCOLO_APOLO_001: {self.powers.abilities['Poder Psicológico']} em nível MÁXIMO. Status: VERDE.",
            f"COMANDO_{self.role.upper()}_{random.randint(100, 999)}: Força Bélica de {self.powers.force_level} acionada. SYNC: OK.",
            f"AÇÃO_AI_VOLIÇÃO_CONFIRM: {self.powers.abilities.get('Habilidade Especial', 'Prontidão tática')} verificada."
        ]
        return random.choice(phrases)
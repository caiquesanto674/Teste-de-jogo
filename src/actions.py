from enum import Enum, auto

class ActionType(Enum):
    """Enum para representar os tipos de ações que uma unidade pode realizar."""
    ATTACK_NORMAL = auto()
    ATTACK_AGGRESSIVE = auto()
    ATTACK_SPECIAL = auto()
    FLEE = auto()
    SEEK_SUPPORT = auto()
    HEAL = auto()
    IDLE = auto()
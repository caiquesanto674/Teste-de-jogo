from enum import Enum

class ResourceType(Enum):
    METAL = "Metal"
    ENERGY = "Energy"
    CREDITS = "Credits"
    RESEARCH = "Research"

class UnitType(Enum):
    INFANTRY = "Infantry"
    ARMORED = "Armored"
    AIRFORCE = "Airforce"
    PSYCHOLOGICAL = "Psychological"

class MissionState(Enum):
    NEUTRAL = 0
    COMBAT = 1
    DEFENSE = 2
    RESEARCH = 3
    DIPLOMACY = 4

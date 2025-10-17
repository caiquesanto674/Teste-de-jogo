import random
import datetime
import logging
from enum import Enum
from typing import Dict, List, Optional, Any

# Global Settings
LOG_FILE = "aurora_galaxy_advance.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(module)s.%(funcName)s:%(lineno)d - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8'), logging.StreamHandler()]
)

def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(val, max_val))

def get_confirmation_phrase(phrase_type: str) -> str:
    phrases = {
        "romance": [
            "The bond strengthened them both. Energy restored.",
            "The emotional bond is your secret shield.",
            "Relationships enhance your mental resilience.",
        ],
        "management": [
            "Report: Population satisfied. Production boosted.",
            "Efficient management: the base is stable.",
        ],
        "technology": [
            "New scientific breakthrough: intelligence enhanced.",
            "Systems optimized, AI reinforced.",
        ]
    }
    return random.choice(phrases.get(phrase_type, ["Action successfully registered."]))

class Action(Enum):
    ROMANCE = "5"
    MANAGEMENT = "6"

# Game Classes

class CompanionAnimal:
    def __init__(self, name, species, attack_bonus, special_power, psychic_damage_bonus=5):
        self.name = name
        self.species = species
        self.attack_bonus = attack_bonus
        self.special_power = special_power
        self.strength_level = 1
        self.psychic_damage_bonus = psychic_damage_bonus

    def apply_bonus(self, character: 'BaseCharacter'):
        character.base_attack += self.attack_bonus * self.strength_level
        character.total_psychic_damage += self.psychic_damage_bonus * self.strength_level
        logging.info(f"{self.name} granted attack and psychic bonuses.")

class Ability:
    def __init__(self, name, type, energy_cost, damage_multiplier, psychic_damage=0, description="", material=None):
        self.name = name
        self.type = type
        self.energy_cost = energy_cost
        self.damage_multiplier = damage_multiplier
        self.psychic_damage = psychic_damage
        self.description = description
        self.material = material

class BaseCharacter:
    STATUS_BONUS = {"Friendship": 0.5, "Romance": 0.8, "Commitment": 1.2, "Lineage": 2.5}

    def __init__(self, name, gender, health=100, attack=10, energy=100, morale=100):
        self.name = name
        self.gender = gender
        self.max_health = health
        self.current_health = health
        self.base_attack = attack
        self.max_morale = morale
        self.morale = morale
        self.base_psychic_defense = 5
        self.bonus_psychic_defense = 0
        self.total_psychic_damage = 5
        self.passive_power = "Mental Focus"
        self.lineage_rank = 1
        self.lineage_bonus = 1.0

    def take_psychic_damage(self, damage):
        defense = self.base_psychic_defense + self.bonus_psychic_defense
        effective_damage = max(0, damage - defense)
        self.morale = clamp(self.morale - effective_damage, 0, self.max_morale)
        logging.info(f"{self.name}: suffered {effective_damage} psychic damage.")

class Ally(BaseCharacter):
    def __init__(self, name, specialty, health=190, attack=15, passive_power="Support Aura"):
        super().__init__(name, "F", health, attack, morale=140)
        self.specialty = specialty
        self.affinity = 10
        self.relationship_status = 'Friendship'
        self.lineage_rank = 2
        self.passive_power = passive_power
        self.recalculate_bonuses()

    def _update_relationship_status(self):
        if self.affinity >= 80:
            self.relationship_status = 'Commitment'
        elif self.affinity >= 40:
            self.relationship_status = 'Romance'
        else:
            self.relationship_status = 'Friendship'

    def recalculate_bonuses(self):
        self._update_relationship_status()
        multiplier = self.STATUS_BONUS.get(self.relationship_status, 0.1)
        self.bonus_psychic_defense = int(self.lineage_rank * 5 * multiplier)

    def interact(self):
        self.affinity = clamp(self.affinity + 15, 10, 100)
        logging.info(get_confirmation_phrase("romance"))
        self.recalculate_bonuses()

class Protagonist(BaseCharacter):
    def __init__(self, name="Kael Aurion"):
        super().__init__(name, "M", health=500, attack=50, energy=150, morale=200)
        self.influence = 50
        self.lineage_rank = 3
        self.lineage_bonus = self.STATUS_BONUS["Lineage"]
        self.companion_animal = CompanionAnimal("Umbra", "Stellar Lynx", 10, "Psychic Illusion")
        self.abilities = [
            Ability("Void Slash", "Attack", 20, 1.5, psychic_damage=0.5, material="Crystallized Ether"),
            Ability("Ion Shield", "Psychic", 10, 0.1, psychic_damage=5.0)
        ]
        self.allies = [
            Ally("Sydra Ryl", "Strategic Warrior"),
            Ally("Lyra Melian", "Arcanist"),
        ]
        self.companion_animal.apply_bonus(self)

    def recalculate_ally_bonuses(self):
        self.bonus_psychic_defense = sum(ally.bonus_psychic_defense for ally in self.allies)

    def consume_resource(self, resource):
        if resource == "Rare Food":
            self.morale = self.max_morale
            logging.info("Restored all morale and health.")
        elif resource == "Crystallized Ether":
            self.total_psychic_damage += 5
            logging.info("Permanently increased psychic damage.")

    def research_technology(self, tech_type, technology):
        if tech_type == "Psychic Defense":
            self.base_psychic_defense += 10
            technology.upgrade_defense()
        elif tech_type == "Warfare Attack":
            self.base_attack += 15
            technology.upgrade_attack()

    def perform_action(self, action, base):
        if action == Action.ROMANCE:
            target = random.choice(self.allies)
            target.interact()
            self.recalculate_ally_bonuses()
        elif action == Action.MANAGEMENT:
            impact = random.randint(5, 15)
            base.apply_morale_impact(impact)
            logging.info(get_confirmation_phrase("management"))

class EnemyFaction(BaseCharacter):
    def __init__(self, name="Order of the Shadowy Veil", power_path="Dimensional Corruption", military_force=500, influence=50):
        super().__init__(name, "N", health=1000, attack=military_force, morale=200)
        self.power_path = power_path
        self.lineage_rank = 4
        self.passive_power = "Global Psychic Disturbance"
        self.total_psychic_damage = 100

    def calculate_offensive_power(self):
        total_power = int(self.base_attack * (self.morale / 100))
        psychic_damage = int(self.total_psychic_damage * (self.morale / 100))
        return {"Total_Power": total_power, "Effective_Psychic_Damage": psychic_damage}

class MilitaryBase:
    def __init__(self, name="Solaris Stronghold"):
        self.name = name
        self.level = 1
        self.max_pleb_morale = 100
        self.pleb_morale = 75
        self.resources = {"Shock": 50000, "Metal": 1000, "Energy": 2000, "Rare Food": 5, "Crystallized Ether": 2}

    def apply_morale_impact(self, impact):
        self.pleb_morale = clamp(self.pleb_morale + impact, 0, self.max_pleb_morale)
        if self.pleb_morale <= 10:
            logging.warning("Pleb morale collapsing — production penalty!")
        logging.info(f"New pleb morale: {self.pleb_morale}")

class Economy:
    def __init__(self):
        self.base_production_rate = {"Shock": 1000, "Metal": 100, "Energy": 50, "Rare Food": 1, "Crystallized Ether": 0}

    def collect_resources(self, base: MilitaryBase):
        morale_factor = max(0.25, base.pleb_morale / base.max_pleb_morale)
        for res, qty in self.base_production_rate.items():
            base.resources[res] += int(qty * morale_factor)
            logging.info(f"Base collected {res}: +{int(qty * morale_factor)} (Morale: {base.pleb_morale})")

class Technology:
    def __init__(self):
        self.defense_level = 1
        self.attack_level = 1

    def upgrade_defense(self):
        self.defense_level += 1
        logging.info(get_confirmation_phrase("technology"))

    def upgrade_attack(self):
        self.attack_level += 1
        logging.info(get_confirmation_phrase("technology"))

class TacticalAI:
    def recommend_action(self, protagonist: Protagonist, base: MilitaryBase, enemy: EnemyFaction):
        if base.pleb_morale < 40:
            return Action.MANAGEMENT
        if protagonist.bonus_psychic_defense < 12:
            return Action.ROMANCE
        if enemy.total_psychic_damage > 95:
            return Action.MANAGEMENT
        return random.choice([Action.ROMANCE, Action.MANAGEMENT])

class GameSimulator:
    def __init__(self):
        self.protagonist = Protagonist()
        self.enemy = EnemyFaction()
        self.base = MilitaryBase()
        self.economy = Economy()
        self.technology = Technology()
        self.ai = TacticalAI()

    def simulate_turn(self):
        action = self.ai.recommend_action(self.protagonist, self.base, self.enemy)
        self.economy.collect_resources(self.base)
        if action:
            self.protagonist.perform_action(action, self.base)
        psychic_damage = int(self.enemy.calculate_offensive_power()["Effective_Psychic_Damage"] * 0.1)
        self.base.apply_morale_impact(-psychic_damage)

    def summary_status(self):
        print(f"Protagonist: {self.protagonist.name} | Morale: {self.protagonist.morale} | Psychic Defense: {self.protagonist.base_psychic_defense + self.protagonist.bonus_psychic_defense}")
        print(f"Base: {self.base.name} | Pleb Morale: {self.base.pleb_morale}")
        print(f"Enemy: {self.enemy.name} | Attack: {self.enemy.base_attack}")

# Execution
if __name__ == "__main__":
    random.seed(42)  # Reproducibility for testing
    sim = GameSimulator()
    for i in range(3):
        print(f"--- Turn {i+1} ---")
        sim.simulate_turn()
        sim.summary_status()
from .ai_system import PPOAgent
from .movement_system import Position

class BaseCharacter:
    def __init__(self, name: str, health: int = 100, attack: int = 10, morale: int = 100):
        self.name = name
        self.max_health = health
        self.base_health = health
        self.current_health = health
        self.base_attack = attack
        self.current_attack = attack
        self.max_morale = morale
        self.morale = morale
        self.psi_bonus = 1.0
        self.tech_bonus = 1.0
        self.position = Position(0, 0)

    def apply_bonuses(self, tech_bonus: float, psi_bonus: float):
        self.tech_bonus = tech_bonus
        self.psi_bonus = psi_bonus
        self.current_attack = self.base_attack * tech_bonus * psi_bonus
        self.max_health = self.base_health * tech_bonus

class Protagonist(BaseCharacter):
    def __init__(self, name: str = "Kael Aurion"):
        super().__init__(name, health=500, attack=50, morale=200)
        self.allies = []
        self.influence = 50
        self.lineage_rank = 3
        self.ppo_agent = PPOAgent()

    def add_ally(self, ally: 'Ally'):
        self.allies.append(ally)
        ally.apply_romance_bonus(self)

class Ally(BaseCharacter):
    def __init__(self, name: str, specialty: str):
        super().__init__(name, health=190, attack=15, morale=140)
        self.specialty = specialty
        self.affinity = 10
        self.status = "Friendship"

    def interact_romance(self):
        self.affinity = min(100, self.affinity + 15)
        if self.affinity >= 80:
            self.status = "Commitment"
            self.psi_bonus = 1.5
        elif self.affinity >= 40:
            self.status = "Romance"
            self.psi_bonus = 1.2
        return self.affinity / 100 * 0.8  # Reward

    def apply_romance_bonus(self, protagonist: Protagonist):
        bonus_defense = len(protagonist.allies) * 5 * self.psi_bonus
        protagonist.morale += bonus_defense

class EnemyFaction(BaseCharacter):
    def __init__(self):
        super().__init__("Order of the Shadowy Veil", health=1000, attack=500, morale=200)
        self.psychic_damage = 100

    def psychic_attack(self, base: 'galaxia_aurora_v20.core.base_system.MilitaryBase'):
        damage = int(self.psychic_damage * 0.1 * (self.morale / 100))
        base.apply_impact(-damage)
        return damage

class MilitaryUnit(BaseCharacter):
    def __init__(self, name, attack, hp, ai_agent):
        """Initializes a military unit."""
        super().__init__(name, health=hp, attack=attack)
        self.hp = self.max_hp = hp
        self.ai = ai_agent
        self.nearby_enemies = 0
        self.support = None

    def perform_action(self, target, support):
        """Executes an action based on the AI's decision."""
        context = {
            'unit': self,
            'target': target,
            'support': support,
            'action': ActionType.COMBAT,
            'BT_ROOT': self.bt()
        }
        action = self.ai.decide_action(context)
        if action == "ATAQUE_AGR":
            return f"{self.name} aggressive attack!", 1.0
        if action == "FUGIR":
            return f"{self.name} retreats!", 0.5
        if action == "BUSCAR_SUPORTE":
            self.hp = clamp(self.hp + 30, 0, self.max_hp)
            return f"{self.name} seeks support and heals.", 0.8
        return f"{self.name} normal attack.", 0.2

    def bt(self):
        """Defines the unit's behavior tree."""
        return SelectorNode("Main",
            SequenceNode("Survival", RetreatAction("Retreat")),
            SequenceNode("Support", SeekSupportAction("Seek Support")),
            AttackAction("Attack")
        )

class SupportUnit(MilitaryUnit):
    def perform_action(self, target, support):
        """Heals an allied unit."""
        if target.hp < 70:
            target.hp = clamp(target.hp + 20, 0, target.max_hp)
        return f"{self.name} heals {target.name}."
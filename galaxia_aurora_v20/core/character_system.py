from .ai_system import PPOAgent, ActionType, SelectorNode, SequenceNode, RetreatAction, SeekSupportAction, AttackAction
from .movement_system import Position

def clamp(value, min_value, max_value):
    """Clamps a value between a minimum and a maximum."""
    return max(min_value, min(value, max_value))

class BaseCharacter:
    def __init__(self, name, health=100, attack=10, morale=100):
        self.name = name
        self.max_health = self.base_health = health
        self.current_health = health
        self.base_attack = self.current_attack = attack
        self.max_morale = self.morale = morale
        self.psi_bonus = 1.0
        self.tech_bonus = 1.0
        self.position = None # Will be a Position object

class Protagonist(BaseCharacter):
    def __init__(self, name="Kael Aurion"):
        super().__init__(name, health=500, attack=50, morale=200)
        self.allies = []
        self.ppo_agent = PPOAgent()

    def add_ally(self, ally):
        self.allies.append(ally)

class Ally(BaseCharacter):
    def __init__(self, name, specialty):
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

    def apply_romance_bonus(self, protagonist: "Protagonist"):
        bonus_defense = len(protagonist.allies) * 5 * self.psi_bonus
        protagonist.morale += bonus_defense

class EnemyFaction(BaseCharacter):
    def __init__(self, name="Order of the Shadowy Veil"):
        super().__init__(name, health=1000, attack=500, morale=200)
        self.psychic_damage = 100

    def psychic_attack(self, base: 'galaxia_aurora_v20.core.base_system.MilitaryBase'):
        damage = int(self.psychic_damage * 0.1 * (self.morale / 100))
        base.apply_morale_impact(-damage)
        return damage

class MilitaryUnit(BaseCharacter):
    def __init__(self, name, attack, hp, ai_agent):
        super().__init__(name, health=hp, attack=attack)
        self.ai_agent = ai_agent
        self.support = None

    def perform_action(self, target, support):
        context = {
            'unit': self, 'target': target, 'support': support,
            'action': ActionType.COMBAT, 'bt_root': self.get_behavior_tree()
        }
        action = self.ai_agent.decide_action(context)
        # Action logic...
        return f"{self.name} performs {action.name}", 0.5

    def get_behavior_tree(self):
        return SelectorNode("Main",
            SequenceNode("Survival", RetreatAction("Retreat")),
            SequenceNode("Support", SeekSupportAction("Seek Support")),
            AttackAction("Attack")
        )

class SupportUnit(MilitaryUnit):
    def perform_action(self, target, support):
        # ... Healing logic
        return f"{self.name} heals {target.name}."
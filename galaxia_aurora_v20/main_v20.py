import random
import logging
from datetime import datetime

from .core.ai_system import DecisionAI, PPOAgent, ActionType
from .core.character_system import Protagonist, Ally, EnemyFaction, MilitaryUnit, SupportUnit
from .core.base_system import MilitaryBase
from .core.economy_system import Economy
from .core.technology_system import TechnologySystem
from .core.correction_system import VestcarSystem
from .core.movement_system import GameMap, Position
from .integrations.firebase_bridge import FirebaseBridge
from .integrations.happymod_api import HappyModAPI

class GameEngine:
    def __init__(self):
        self.vestcar = VestcarSystem()
        self.firebase = FirebaseBridge()
        self.happymod = HappyModAPI()
        self.protagonist = Protagonist("Kael Aurion")
        self.base = MilitaryBase()
        self.enemy = EnemyFaction()
        self.economy = Economy()
        self.technology = TechnologySystem()
        self.map = GameMap(100, 100)

        # Initial Setup
        self.map.add_entity(self.protagonist, Position(10, 10))
        self.map.add_entity(self.base, Position(0, 0))
        self.map.add_entity(self.enemy, Position(90, 90))

        self.protagonist.add_ally(Ally("Sydra Ryl", "Strategic"))
        random.seed(42)

    def calculate_context(self) -> dict:
        return {
            "average_affinity": sum(a.affinity for a in self.protagonist.allies) / len(self.protagonist.allies) if self.protagonist.allies else 0,
            "pleb_morale": self.base.morale,
            "tech_level": sum(t["level"] for t in self.technology.tree.values()),
            "enemy_hp_ratio": self.enemy.current_health / self.enemy.max_health,
            "distance_to_enemy": self.map.get_distance(self.protagonist.position, self.enemy.position)
        }

    def run_turn(self, turn: int):
        context = self.calculate_context()

        # 1. AI decides
        scores = {action: DecisionAI.score_action(action, context) for action in ActionType}
        chosen_action = self.protagonist.ppo_agent.decide_action(scores, context)

        # 2. Execute action
        reward = self._execute_action(chosen_action)
        self.protagonist.ppo_agent.learn(chosen_action, reward)

        # 3. Economy + Technology
        self.economy.generate_resources(self.base)
        self.technology.apply_bonuses(self.base, self.protagonist)

        # 4. Enemy attacks
        enemy_damage = self.enemy.psychic_attack(self.base)

        # 5. VESTCAR protects
        corrections = self.vestcar.protect_unit(self.protagonist)
        corrections += self.vestcar.protect_unit(self.base)

        # 6. Log + Phrase
        phrase = self.vestcar.get_confirmation_phrase(chosen_action.name.lower())

        return {
            "action": chosen_action.name,
            "reward": reward,
            "enemy_damage": enemy_damage,
            "vestcar_corrections": corrections,
            "base_morale": self.base.morale,
            "phrase": phrase
        }

    def _execute_action(self, action: ActionType) -> float:
        if action == ActionType.ROMANCE:
            ally = random.choice(self.protagonist.allies)
            reward = ally.interact_romance()
            self.protagonist.morale += 10
        elif action == ActionType.MANAGEMENT:
            impact = random.randint(5, 15)
            self.base.apply_impact(impact)
            reward = 0.7 if self.base.morale > 50 else 0.3
        elif action == ActionType.TECHNOLOGY:
            success = self.technology.research("Psi_Defense", self.base.resources)
            reward = 0.9 if success else 0.2
        elif action == ActionType.MOVE:
            # Simple move towards enemy
            new_x = self.protagonist.position.x + 1
            new_y = self.protagonist.position.y + 1
            self.map.move_entity(self.protagonist, Position(new_x, new_y))
            reward = 0.5
        else: # COMBAT and SUPPORT
            # The combat and support logic is handled by the MilitaryUnit
            reward = 0.5

        return reward

def main():
    """Main function to simulate the game."""
    engine = GameEngine()
    for i in range(5):
        print(f"\n--- TURN {i+1} ---")
        turn_result = engine.run_turn(i + 1)
        print(f"Action: {turn_result['action']} | Phrase: {turn_result['phrase']}")

if __name__ == "__main__":
    main()
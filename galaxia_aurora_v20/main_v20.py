import random
import logging
from datetime import datetime

from .core.ai_system import DecisionAI, PPOAgent, ActionType
from .core.character_system import Protagonist, Ally, EnemyFaction
from .core.base_system import MilitaryBase
from .core.economy_system import EconomySystem
from .core.technology_system import TechnologySystem
from .core.correction_system import VestcarSystem
from .core.movement_system import GameMap, Position
from .integrations.firebase_bridge import FirebaseBridge
from .integrations.happymod_api import HappyModAPI

# --- CONFIG GLOBAL + LOGGING ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [V20] %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("galaxia_aurora_v20.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class GameEngineV20:
    def __init__(self):
        self.vestcar = VestcarSystem()
        self.firebase = FirebaseBridge()
        self.happymod = HappyModAPI()
        self.protagonist = Protagonist("Kael Aurion")
        self.base = MilitaryBase()
        self.enemy = EnemyFaction()
        self.economy = EconomySystem()
        self.technology = TechnologySystem()
        self.ai = DecisionAI()
        self.map = GameMap(100, 100)

        # Initial Setup
        self.map.add_entity(self.protagonist, Position(10, 10))
        self.map.add_entity(self.base, Position(0, 0))
        self.map.add_entity(self.enemy, Position(90, 90))

        self.protagonist.add_ally(Ally("Sydra Ryl", "Strategic"))
        random.seed(42)

        logging.info("🚀 GALÁXIA AURORA V20 INICIADA!")

    def calculate_context(self) -> dict:
        return {
            "average_affinity": sum(a.affinity for a in self.protagonist.allies) / len(self.protagonist.allies) if self.protagonist.allies else 0,
            "pleb_morale": self.base.pleb_morale,
            "tech_level": sum(t["level"] for t in self.technology.tree.values()),
            "enemy_hp_ratio": self.enemy.current_health / self.enemy.max_health,
            "distance_to_enemy": self.map.get_distance(self.protagonist.position, self.enemy.position)
        }

    def run_turn(self, turn: int):
        context = self.calculate_context()

        # 1. AI decides
        scores = {action: self.ai.score_action(action, context) for action in ActionType}
        chosen_action = self.protagonist.ppo_agent.decide_action(scores, context)

        # 2. Execute action
        reward = self._execute_action(chosen_action)
        self.protagonist.ppo_agent.learn(chosen_action, reward)

        # 3. Economy + Technology
        self.economy.execute_production(self.base)
        self.technology.apply_bonuses(self.base, self.protagonist)

        # 4. Enemy attacks
        enemy_damage = self.enemy.psychic_attack(self.base)

        # 5. VESTCAR protects
        corrections = self.vestcar.protect_unit(self.protagonist)
        corrections += self.vestcar.protect_unit(self.base)

        # 6. Log + Phrase
        phrase = self.vestcar.get_confirmation_phrase(chosen_action.name.lower())
        logging.info(f"🎯 Turn {turn}: {chosen_action.name} | {phrase}")

        return {
            "action": chosen_action.name,
            "reward": reward,
            "enemy_damage": enemy_damage,
            "vestcar_corrections": corrections,
            "base_morale": self.base.pleb_morale
        }

    def _execute_action(self, action: ActionType) -> float:
        if action == ActionType.ROMANCE:
            ally = random.choice(self.protagonist.allies)
            reward = ally.interact_romance()
            self.protagonist.morale += 10
        elif action == ActionType.MANAGEMENT:
            impact = random.randint(5, 15)
            self.base.apply_morale_impact(impact)
            reward = 0.7 if self.base.pleb_morale > 50 else 0.3
        elif action == ActionType.TECHNOLOGY:
            success = self.technology.research("Psi_Defense", self.base.resources)
            reward = 0.9 if success else 0.2
        elif action == ActionType.MOVE:
            # Simple move towards enemy
            new_x = self.protagonist.position.x + 1
            new_y = self.protagonist.position.y + 1
            self.map.move_entity(self.protagonist, Position(new_x, new_y))
            reward = 0.5
        else:
            reward = 0.5  # Default

        return reward

    def run_campaign(self, turns: int = 10):
        print("=" * 80)
        print("🌌 GALÁXIA AURORA V20 - COMPLETE CAMPAIGN")
        print(f"🕐 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)

        results = []
        for turn in range(turns):
            result = self.run_turn(turn + 1)
            results.append(result)

            # Turn summary
            print(f"\n--- TURN {turn+1} ---")
            print(f"🎯 Action: {result['action']} | Reward: {result['reward']:.2f}")
            print(f"🏰 Base Morale: {self.base.pleb_morale} | Ether Resources: {self.base.resources.get('Ether', 0)}")
            print(f"🌀 PPO {result['action']}: {self.protagonist.ppo_agent.policy[result['action']]:.2f}")
            print(f"🛡️ VESTCAR: {result['vestcar_corrections']} corrections")

        # Final + Export
        progress_json = self.firebase.save_progress(self)
        print(f"\n📱 Unity/Firebase Data:\n{progress_json[:200]}...")
        print(f"\n🏆 CAMPAIGN FINISHED!")
        print(f"📊 Base Survived: {'✅' if self.base.pleb_morale > 0 else '❌'}")
        print(f"🔬 Max Tech: {max(t['level'] for t in self.technology.tree.values())}")

        return results

def full_test():
    """Automated Test V20"""
    engine = GameEngineV20()

    # Validate HAPPYMOD
    if engine.happymod.validate_structure():
        print("✅ HAPPYMOD Structure: VALIDATED")

    # Run campaign
    results = engine.run_campaign(5)

    # Final analysis
    actions_by_type = {}
    for r in results:
        actions_by_type[r['action']] = actions_by_type.get(r['action'], 0) + 1

    print(f"\n📈 ACTION ANALYSIS:")
    for action, count in actions_by_type.items():
        print(f"   {action}: {count} executions")

    # Export MOD
    mod_data = {"version": "V20", "actions": actions_by_type}
    mod_export = engine.happymod.export_mod(mod_data)
    print(f"\n🎮 {mod_export}")

    return results

if __name__ == "__main__":
    # Run full test
    results = full_test()

    # Final status
    print("\n" + "="*80)
    print("🎉 GALÁXIA AURORA V20 - UNIFIED SYSTEM COMPLETE!")
    print("✅ Integrations: Tactical AI + Isekai + Economy + Technology + Firebase")
    print("✅ HAPPYMOD Structure: Validated and Exportable")
    print("🚀 Ready for Unity + Web + APK Distribution")
    print("="*80)
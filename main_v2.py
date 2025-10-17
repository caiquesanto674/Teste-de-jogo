import random
import math
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import logging

# --- GLOBAL CONFIGURATION AND LOGGING ---
LOG_FILE = "core_nexus_aurora_v10.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(module)s.%(funcName)s:%(lineno)d - %(message)s',
    handlers=[logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8'), logging.StreamHandler()]
)

def clamp(val: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(val, max_val))

from enum import Enum

# =========================================================================
# MODULE 1: ADVANCED TACTICAL AI (Utility AI, BT, PPO - V8)
# =========================================================================

class CombatAction(Enum):
    NORMAL_ATTACK = "NORMAL_ATTACK"
    AGGRESSIVE_ATTACK = "AGGRESSIVE_ATTACK"
    SEEK_SUPPORT = "SEEK_SUPPORT"
    HEAL_ALLY = "HEAL_ALLY"
    AWAIT_ORDER = "AWAIT_ORDER"

class StrategicAction(Enum):
    PLEB_MANAGEMENT = "PLEB_MANAGEMENT"
    ALLY_INTERACTION = "ALLY_INTERACTION"
    INVEST_IN_ECONOMY = "INVEST_IN_ECONOMY"
    MILITARY_TRAINING = "MILITARY_TRAINING"

class DecisionAI:
    """Utility AI: Scoring functions for tactical actions."""
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    @staticmethod
    def score_seek_health(own_health, available_resources):
        score = (100 - own_health) * (1 if available_resources > 0 else 0)
        return DecisionAI.sigmoid(score / 50.0)

class PPOAgent:
    """Reinforcement Learning: Adjusts tactical 'psychology'."""
    def __init__(self, hyperparameters):
        self.policy = {'AGGRESSIVE_ATTACK_STRENGTH': 0.5}
        self.hyperparameters = hyperparameters
    def update_policy(self, state_key, reward):
        current_strength = self.policy.get(state_key, 0.5)
        new_strength = current_strength + reward * self.hyperparameters.get('learning_rate', 0.05)
        self.policy[state_key] = min(1.0, max(0.0, new_strength))

    # Placeholder: To simplify unification, BT is executed outside of PPO.
    def get_optimized_action(self, bt_action: CombatAction) -> CombatAction:
        if bt_action == CombatAction.NORMAL_ATTACK:
            if self.policy.get('AGGRESSIVE_ATTACK_STRENGTH', 0.5) > 0.8:
                return CombatAction.AGGRESSIVE_ATTACK
        return bt_action

# Behavior Tree classes (simplified for integration)
class BehaviorNode:
    def __init__(self, name="Node"):
        self.name = name
    def execute(self, unit, context): pass

class Selector(BehaviorNode):
    def __init__(self, nodes, name="Selector"):
        super().__init__(name)
        self.nodes = nodes

    def execute(self, unit, context):
        for node in self.nodes:
            if node.execute(unit, context) == "SUCCESS":
                return "SUCCESS"
        return "FAILURE"

class Sequence(BehaviorNode):
    def __init__(self, nodes, name="Sequence"):
        super().__init__(name)
        self.nodes = nodes

    def execute(self, unit, context):
        for node in self.nodes:
            if node.execute(unit, context) == "FAILURE":
                return "FAILURE"
        return "SUCCESS"

# BT Actions (These actions use Utility AI to decide if the BT progresses)
class SeekSupportAction(BehaviorNode):
    def __init__(self, name="Seek Support"):
        super().__init__(name)

    def execute(self, unit, context):
        if context['support_ally'].current_health > 0 and unit.current_health < 50:
            prob = DecisionAI.score_seek_health(unit.current_health, 1) # 1=Resource available
            if prob > 0.5:
                context['selected_action'] = CombatAction.SEEK_SUPPORT
                return "SUCCESS"
        return "FAILURE"

# =========================================================================
# MODULE 2: CHARACTER, ALLIES, AND COMBAT (RPG/PSYCHOLOGICAL - Refined)
# =========================================================================

class BaseCharacter:
    def __init__(self, name, health=100, attack=10, morale=100):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.base_attack = attack
        self.max_morale = morale
        self.morale = morale
        self.bonus_psychic_defense = 0
        self.total_psychic_damage = 5

    def take_psychic_damage(self, damage):
        effective_damage = max(0, damage - self.bonus_psychic_defense)
        self.morale = clamp(self.morale - effective_damage, 0, self.max_morale)
        logging.info(f"{self.name}: suffered {effective_damage} psychic damage. Morale: {self.morale}")

# The Protagonist inherits the AI capability of their Units/Subordinates.
class Protagonist(BaseCharacter): # Kael Aurion / Caíque
    STATUS_BONUS = {"Friendship": 0.5, "Romance": 0.8, "Lineage": 2.5}
    def __init__(self, name="Kael Aurion (Caíque)"):
        super().__init__(name, health=500, attack=50, morale=200)
        self.allies: List[Ally] = []
        self.companion_animal = CompanionAnimal("Umbra", "Stellar Lynx", 10)
        self.companion_animal.apply_bonus(self)

    def recalculate_ally_bonuses(self):
        self.bonus_psychic_defense = sum(ally.bonus_psychic_defense for ally in self.allies)

class Ally(BaseCharacter): # Sydra / Lyra
    def __init__(self, name, affinity=10):
        super().__init__(name, health=190, attack=15, morale=140)
        self.affinity = affinity
        self.relationship_status = 'Friendship'
        self.bonus_psychic_defense = 5

    def interact(self, protagonist: Protagonist):
        self.affinity = clamp(self.affinity + 15, 10, 100)
        protagonist.morale = clamp(protagonist.morale + 10, 0, protagonist.max_morale)
        logging.info(f"Bond with {self.name} strengthened. {protagonist.name}'s morale recovered.")

class CompanionAnimal:
    def __init__(self, name, species, attack_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
    def apply_bonus(self, character: Protagonist):
        character.base_attack += self.attack_bonus

# Class that implements the Combat BT/PPO (Real Battle Unit)
class MilitaryUnit(BaseCharacter):
    def __init__(self, name, base_attack, base_hp, ai_agent: PPOAgent):
        super().__init__(name, health=base_hp, attack=base_attack)
        self.ai_agent = ai_agent
        self.bt_root = self._get_behavior_tree()

    # CENTRAL COMMUNICATION FUNCTION V10
    def make_ai_decision(self, target_enemy: BaseCharacter, support_ally: 'SupportUnit') -> CombatAction:
        """Complete Decision Process: Utility AI -> BT -> PPO."""

        # 1. STATE MONITORING AND BT CONTEXT
        context = {
            'unit': self, 'target': target_enemy, 'support_ally': support_ally,
            'selected_action': CombatAction.NORMAL_ATTACK,
        }

        # 2. BT EXECUTION (Utility AI decides if the node succeeds)
        self.bt_root.execute(self, context)
        bt_action = context['selected_action']

        # 3. PPO COMMUNICATION AND ADJUSTMENT
        final_action = self.ai_agent.get_optimized_action(bt_action)

        # 4. MONITORING AND CONFIRMATION
        print(f"\n[{self.name} - AI CONFIRMATION CODE]: {self._generate_ai_confirmation_phrase(final_action)}")
        logging.info(f"AI Decision: {final_action.value} (PPO: {self.ai_agent.policy['AGGRESSIVE_ATTACK_STRENGTH']:.2f})")
        return final_action

    def _get_behavior_tree(self):
        """Simplified BT: Prioritizes Support/Healing if the ally is alive."""

        class AttackAction(BehaviorNode):
            def execute(self, unit, context):
                context['selected_action'] = CombatAction.NORMAL_ATTACK
                return "SUCCESS"

        # Using a simple selector for now. A more complex BT would have more nodes.
        return Selector(nodes=[
            SeekSupportAction("Tactical Recovery"),
            AttackAction("Direct Attack")
        ])


    def _generate_ai_confirmation_phrase(self, action: CombatAction):
        """Behavior phrases in confirmation code (From your initial code)."""
        phrases = {
            CombatAction.AGGRESSIVE_ATTACK: "PROTOCOL_OFFENSIVE_ALPHA: Confirmed. Maximum Damage. Superior Warfare Level Activated.",
            CombatAction.SEEK_SUPPORT: "PROTOCOL_LOGISTIC_RECALL: Confirmed. Tactical Repair Request. Priority 1: Unit Integrity.",
            CombatAction.NORMAL_ATTACK: "PROTOCOL_COMBAT_STANDARD: Confirmed. Standard Engagement."
        }
        return phrases.get(action, "PROTOCOL_UNKWN_ZETA: Recalibrating.")

class SupportUnit(MilitaryUnit):
    """New Logistic Support unit, with priority healing logic."""
    def __init__(self, name, base_attack, base_hp, ai_agent: PPOAgent):
        super().__init__(name, base_attack, base_hp, ai_agent)

    def make_ai_decision(self, combat_target, main_ally: MilitaryUnit) -> CombatAction:
        if main_ally.current_health < main_ally.max_health * 0.7:
            main_ally.current_health = clamp(main_ally.current_health + 20, 0, main_ally.max_health)
            print(f"[{self.name}]: HEALING ACTIVATED! {main_ally.name} HP Restored.")
            return CombatAction.HEAL_ALLY
        return CombatAction.AWAIT_ORDER


# =========================================================================
# MODULE 3: BASE, ECONOMY, AND TECHNOLOGY (Strategic Management)
# =========================================================================

class BaseEconomy:
    def __init__(self, guild_treasury=10000.0):
        self.treasury = guild_treasury
        self.production_rate = 1.0 # Gross resource multiplier

    def produce_resources(self, units: int) -> float:
        revenue = int(units * 150 * self.production_rate)
        self.treasury += revenue
        return revenue

    # Logistic Communication Function (Capital Transfer)
    def transfer_capital(self, destination: 'MilitaryBase', amount: float) -> str:
        if self.treasury >= amount:
            self.treasury -= amount
            destination.military_budget += amount
            return f"[Logistics]: {amount:.2f} Credits transferred to the Military Base. Remaining treasury: {self.treasury:.2f}."
        return "[Logistics]: Transfer Failed. Insufficient treasury."

class Technology:
    def __init__(self):
        self.tech_level = 1
        self.bonus_multiplier = 1.0

    def advance_level(self):
        self.tech_level += 1
        self.bonus_multiplier = 1.0 + (self.tech_level * 0.1)
        logging.info(f"Technology Advanced. Scale Bonus: {self.bonus_multiplier:.2f}x")

class TacticalAnalysisAI:
    """Geopolitical Analysis for the Protagonist (High-Level Decision)."""
    def recommend_action(self, base: 'MilitaryBase', protagonist: Protagonist) -> StrategicAction:
        if base.pleb_morale < 40:
            return StrategicAction.PLEB_MANAGEMENT
        if protagonist.morale < 100:
            return StrategicAction.ALLY_INTERACTION
        if base.resources.get("Shock", 0) < 5000:
            return StrategicAction.INVEST_IN_ECONOMY
        return StrategicAction.MILITARY_TRAINING

class MilitaryBase:
    def __init__(self, name="Solaris Stronghold"):
        self.name = name
        self.military_budget = 0.0
        self.pleb_morale = 75
        self.resources = {"Shock": 50000, "Metal": 1000}
        self.military_troops = 100 # For the K calculation

    def apply_morale_impact(self, impact):
        self.pleb_morale = clamp(self.pleb_morale + impact, 0, 100)

    def calculate_war_force(self, tech_bonus: float) -> float:
        # Formula K = (Resources * Technology_Level) + (Troops)
        K = (self.resources["Metal"] * tech_bonus) + self.military_troops
        return K

# =========================================================================
# MODULE 4: UNIFICATION AND TEST FUNCTION (Cycle Simulation)
# =========================================================================

def start_simulation_v10():
    print("="*80)
    print("CORE NEXUS AURORA V10 SIMULATION STARTED - SYSTEMS UNIFICATION")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)

    # 1. Initialization of Systems and Characters
    economy = BaseEconomy()
    technology = Technology()
    base = MilitaryBase()
    protagonist = Protagonist()
    strategic_ai = TacticalAnalysisAI()

    sydra = Ally("Sydra Ryl")
    lyra = Ally("Lyra Melian")
    protagonist.allies.extend([sydra, lyra])

    ppo_config = {'learning_rate': 0.1}
    infiltrator = MilitaryUnit("Infiltrator-1 (Tactical Caíque)", 20, 100, PPOAgent(ppo_config))
    support = SupportUnit("Support-1", 10, 80, PPOAgent(ppo_config))
    enemy = BaseCharacter("War-AI Enemy", health=120, attack=30)

    # --- CYCLE 1: STRATEGIC PHASE (High-Level AI) ---
    print("\n--- CYCLE 1: STRATEGY AND MANAGEMENT ---")

    # 1.1. STRATEGY COMMUNICATION (Analytical AI)
    high_level_action = strategic_ai.recommend_action(base, protagonist)

    # 1.2. MONITORING AND EXECUTION
    print(f"[STRATEGIC AI]: Recommended Action: {high_level_action.value}")

    if high_level_action == StrategicAction.ALLY_INTERACTION:
        random.choice(protagonist.allies).interact(protagonist)
        protagonist.recalculate_ally_bonuses()

    # 1.3. ECONOMIC PHASE
    economy.produce_resources(100)
    print(economy.transfer_capital(base, 5000.0))
    technology.advance_level()

    # --- CYCLE 2: TACTICAL PHASE (Low-Level AI - Units) ---
    print("\n--- CYCLE 2: TACTICAL COMBAT AND UNIT AI ---")

    # Simulate damage to the Infiltrator to force the AI to seek Support
    infiltrator.current_health = 45
    infiltrator.morale = 15
    support.current_health = 50 # Support HP

    # 2.1. INFILTRATOR'S ACTION (The most critical communication and monitoring line)
    combat_action = infiltrator.make_ai_decision(enemy, support)

    # 2.2. TACTICAL EXECUTION AND REWARD
    if combat_action == CombatAction.SEEK_SUPPORT:
        reward = 0.8
        support.make_ai_decision(enemy, infiltrator) # Support heals
    elif combat_action in [CombatAction.NORMAL_ATTACK, CombatAction.AGGRESSIVE_ATTACK]:
        reward = 1.0 if enemy.current_health <= 0 else 0.2
        enemy.current_health -= infiltrator.base_attack # Deals damage
    else:
        reward = 0.1

    infiltrator.ai_agent.update_policy('AGGRESSIVE_ATTACK_STRENGTH', reward)

    # 2.3. ENEMY'S ACTION
    enemy_psychic_damage = 20
    protagonist.take_psychic_damage(enemy_psychic_damage)

    # --- FINAL SUMMARY ---
    print("\n" + "="*80)
    print("DETAILED SIMULATION SUMMARY (CORE NEXUS AURORA V10)")
    print("="*80)
    print(f"[Protagonist]: {protagonist.name} | Morale: {protagonist.morale:.0f}/{protagonist.max_morale} | Bonus Psychic Defense: {protagonist.bonus_psychic_defense}")
    print(f"[Strategic Base]: Estimated War Force (K): {base.calculate_war_force(technology.bonus_multiplier):.2f}")
    print(f"[Economy/Treasury]: {economy.treasury:.2f} Credits | Tech Level: {technology.tech_level}")
    print(f"[Tactical Unit]: {infiltrator.name} | HP: {infiltrator.current_health}/{infiltrator.max_health} | PPO Aggressiveness: {infiltrator.ai_agent.policy['AGGRESSIVE_ATTACK_STRENGTH']:.2f}")

# --- FINAL EXECUTION ---
if __name__ == "__main__":
    start_simulation_v10()
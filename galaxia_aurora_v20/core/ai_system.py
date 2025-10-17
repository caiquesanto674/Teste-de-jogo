from enum import Enum
import math

class ActionType(Enum):
    ROMANCE = "ROMANCE"
    MANAGEMENT = "MANAGEMENT"
    TECHNOLOGY = "TECHNOLOGY"
    COMBAT = "COMBAT"
    SUPPORT = "SUPPORT"
    MOVE = "MOVE"

class DecisionAI:
    @staticmethod
    def sigmoid(x: float) -> float:
        return 1 / (1 + math.exp(-math.tanh(x)))

    @staticmethod
    def score_action(action_type: ActionType, context: dict) -> float:
        scores = {
            ActionType.ROMANCE: context.get('average_affinity', 0) / 100,
            ActionType.MANAGEMENT: context.get('pleb_morale', 0) / 100,
            ActionType.TECHNOLOGY: context.get('tech_level', 1) / 10,
            ActionType.COMBAT: 1 - (context.get('enemy_hp_ratio', 1.0)),
            ActionType.MOVE: 1 - (context.get('distance_to_enemy', 10) / 20) # Closer is better
        }
        return scores.get(action_type, 0.5)

class PPOAgent:
    def __init__(self):
        """Initializes the agent with an aggressiveness level."""
        self.policy = {
            'ROMANCE': 0.6, 'MANAGEMENT': 0.7, 'TECHNOLOGY': 0.4,
            'COMBAT': 0.5, 'SUPPORT': 0.8, 'MOVE': 0.5
        }

    def decide_action(self, scores: dict, context: dict) -> ActionType:
        best_action = max(scores.items(), key=lambda x: x[1] * self.policy.get(x[0].name, 0.5))[0]
        return best_action

    def learn(self, action: ActionType, reward: float):
        lr = 0.1
        self.policy[action.name] = min(1.0, max(0.0, self.policy.get(action.name, 0.5) + reward * lr))

class BehaviorNode:
    def __init__(self, name):
        """Initializes a behavior node."""
        self.name = name

    def execute(self, unit, context):
        """Method to be implemented in subclasses."""
        raise NotImplementedError

class SelectorNode(BehaviorNode):
    def __init__(self, name, *children):
        super().__init__(name)
        self.children = children

    def execute(self, unit, context):
        """Executes children until one succeeds."""
        for child in self.children:
            if child.execute(unit, context) == "SUCCESS":
                return "SUCCESS"
        return "FAILURE"

class SequenceNode(BehaviorNode):
    def __init__(self, name, *children):
        super().__init__(name)
        self.children = children

    def execute(self, unit, context):
        """Executes children in sequence."""
        for child in self.children:
            if child.execute(unit, context) == "FAILURE":
                return "FAILURE"
        return "SUCCESS"

class AttackAction(BehaviorNode):
    def execute(self, unit, context):
        """Checks if the unit can attack."""
        if unit.current_attack > 10:
            context['action'] = ActionType.COMBAT
            return "SUCCESS"
        return "FAILURE"

class RetreatAction(BehaviorNode):
    def execute(self, unit, context):
        """Checks if the unit should retreat."""
        if unit.hp < 20:
            context['action'] = ActionType.MOVE
            return "SUCCESS"
        return "FAILURE"

class SeekSupportAction(BehaviorNode):
    def execute(self, unit, context):
        """Checks if the unit should seek support."""
        if unit.hp < 50 and context['support'] and context['support'].hp > 0:
            context['action'] = ActionType.SUPPORT
            return "SUCCESS"
        return "FAILURE"
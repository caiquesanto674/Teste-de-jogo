import math
import random
from enum import Enum
from typing import Dict, Any

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
    def score_action(action_type: ActionType, context: Dict) -> float:
        scores = {
            ActionType.ROMANCE: context.get('average_affinity', 0) / 100,
            ActionType.MANAGEMENT: context.get('pleb_morale', 0) / 100,
            ActionType.TECHNOLOGY: context.get('tech_level', 1) / 10,
            ActionType.COMBAT: 1 - (context.get('enemy_hp_ratio', 1.0)),
            ActionType.MOVE: 1 - (context.get('distance_to_enemy', 10) / 20) # Closer is better
        }
        return scores.get(action_type, 0.5)

class BehaviorTreeNode:
    def __init__(self, name: str): self.name = name
    def execute(self, context: Dict) -> str: raise NotImplementedError

class SelectorNode(BehaviorTreeNode):
    def __init__(self, name: str, *children):
        super().__init__(name)
        self.children = children

    def execute(self, context: Dict) -> str:
        for child in self.children:
            if child.execute(context) == "SUCCESS":
                return "SUCCESS"
        return "FAILURE"

class PPOAgent:
    def __init__(self):
        self.policy = {
            'ROMANCE': 0.6, 'MANAGEMENT': 0.7, 'TECHNOLOGY': 0.4,
            'COMBAT': 0.5, 'SUPPORT': 0.8, 'MOVE': 0.5
        }

    def decide_action(self, scores: Dict, context: Dict) -> ActionType:
        best_action = max(scores.items(), key=lambda x: x[1] * self.policy.get(x[0].name, 0.5))[0]
        return best_action

    def learn(self, action: ActionType, reward: float):
        lr = 0.1
        self.policy[action.name] = min(1.0, max(0.0, self.policy.get(action.name, 0.5) + reward * lr))
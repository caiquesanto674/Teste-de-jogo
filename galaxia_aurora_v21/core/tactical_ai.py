from enum import Enum

class ActionType(Enum):
    ATTACK = "ATTACK"
    RETREAT = "RETREAT"
    SEEK_SUPPORT = "SEEK_SUPPORT"

class PPOAgent:
    def __init__(self):
        self.policy = {action.name: 0.5 for action in ActionType}

    def decide_action(self, context: dict) -> ActionType:
        # Simple placeholder logic
        if context.get("health", 100) < 20:
            return ActionType.RETREAT
        return ActionType.ATTACK

    def learn(self, action: ActionType, reward: float):
        lr = 0.1
        current_value = self.policy.get(action.name, 0.5)
        self.policy[action.name] = max(0.0, min(1.0, current_value + reward * lr))

class BehaviorNode:
    def __init__(self, name):
        self.name = name
    def execute(self, unit, context):
        raise NotImplementedError

class SelectorNode(BehaviorNode):
    def __init__(self, name, *children):
        super().__init__(name)
        self.children = children
    def execute(self, unit, context):
        for child in self.children:
            if child.execute(unit, context) == "SUCCESS":
                return "SUCCESS"
        return "FAILURE"

class SequenceNode(BehaviorNode):
    def __init__(self, name, *children):
        super().__init__(name)
        self.children = children
    def execute(self, unit, context):
        for child in self.children:
            if child.execute(unit, context) == "FAILURE":
                return "FAILURE"
        return "SUCCESS"

class AttackAction(BehaviorNode):
    def execute(self, unit, context):
        if unit.attack_power > 10:
            context['action'] = ActionType.ATTACK
            return "SUCCESS"
        return "FAILURE"

class RetreatAction(BehaviorNode):
    def execute(self, unit, context):
        if unit.health < 20:
            context['action'] = ActionType.RETREAT
            return "SUCCESS"
        return "FAILURE"

class SeekSupportAction(BehaviorNode):
    def execute(self, unit, context):
        if unit.health < 50 and context.get('support_available'):
            context['action'] = ActionType.SEEK_SUPPORT
            return "SUCCESS"
        return "FAILURE"
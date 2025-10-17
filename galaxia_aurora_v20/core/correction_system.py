from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class VestcarDiagnosis:
    error_type: str
    corrected_value: float
    unit_name: str
    timestamp: str

class VestcarSystem:
    def __init__(self):
        self.history = []
        self.phrases = {
            "romance": [
                "💖 The bond strengthened them both. Energy restored!",
                "🌟 The emotional bond is your secret shield.",
                "✨ Relationships elevate your mental resilience."
            ],
            "management": [
                "📊 Report: Population satisfied. Production boosted!",
                "🏛️ Efficient management: the base is stable.",
                "⚖️ Balance achieved. Morale restored."
            ],
            "technology": [
                "🔬 New scientific breakthrough: intelligence enhanced!",
                "⚙️ Systems optimized, AI reinforced.",
                "🧬 Technological evolution: unlimited power!"
            ],
            "combat": [
                "⚔️ Tactical victory! Enemy retreats!",
                "🎯 Lethal precision. Objective eliminated!",
                "🛡️ Impenetrable defense maintained!"
            ]
        }

    def protect_unit(self, unit):
        corrections = 0
        if hasattr(unit, 'morale') and unit.morale <= 0:
            unit.morale = 10
            self.history.append(VestcarDiagnosis("CRITICAL_MORALE", 10, unit.name, str(datetime.now())))
            corrections += 1
        if hasattr(unit, 'current_health') and unit.current_health <= 0:
            unit.current_health = max(1, unit.max_health * 0.1)
            corrections += 1
        return corrections

    def get_confirmation_phrase(self, action_type: str) -> str:
        return random.choice(self.phrases.get(action_type, ["✅ Action executed successfully!"]))
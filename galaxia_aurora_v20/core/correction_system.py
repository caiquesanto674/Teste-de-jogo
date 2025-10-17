import random
from datetime import datetime
from typing import Any, List, Dict
from dataclasses import dataclass

@dataclass
class VestcarDiagnosis:
    error_type: str
    corrected_value: float
    unit: str
    timestamp: str

import json

class VestcarSystem:
    def __init__(self, phrases_path="galaxia_aurora_v20/assets/behavior_phrases.json"):
        self.history: List[VestcarDiagnosis] = []
        self.phrases = self._load_phrases(phrases_path)

    def _load_phrases(self, path: str) -> Dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Fallback to default phrases if file is missing or corrupt
            return {
                "romance": ["Default romance phrase"],
                "management": ["Default management phrase"],
                "technology": ["Default technology phrase"],
                "combat": ["Default combat phrase"]
            }

    def protect_unit(self, unit: Any) -> int:
        corrections = 0
        if hasattr(unit, 'morale') and unit.morale <= 0:
            unit.morale = 10
            self.history.append(VestcarDiagnosis("CRITICAL_MORALE", 10, unit.name, str(datetime.now())))
            corrections += 1
        if hasattr(unit, 'current_health') and unit.current_health <= 0:
            unit.current_health = max(1, unit.max_health * 0.1)
            corrections += 1
        return corrections

    def get_confirmation_phrase(self, phrase_type: str) -> str:
        return random.choice(self.phrases.get(phrase_type, ["✅ Action executed successfully!"]))
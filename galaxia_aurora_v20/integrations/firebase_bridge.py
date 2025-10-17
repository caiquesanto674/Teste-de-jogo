import json
import logging
from datetime import datetime
from typing import Dict

class FirebaseBridge:
    def __init__(self):
        self.battle_data = {}

    def save_progress(self, game_engine: 'galaxia_aurora_v20.main_v20.GameEngineV20'):
        data = {
            "protagonist": {"name": game_engine.protagonist.name, "morale": game_engine.protagonist.morale},
            "base": {"pleb_morale": game_engine.base.pleb_morale, "resources": game_engine.base.resources},
            "technology": game_engine.technology.tree,
            "timestamp": datetime.now().isoformat()
        }
        self.battle_data = data
        logging.info(f"☁️ Progress saved: {len(data)} records")
        return json.dumps(data, indent=2)

    def load_lore(self) -> Dict:
        return {
            "lore": "Aurora Galaxy V20: Tactical Isekai with Advanced AI",
            "version": "20.0",
            "tip": "Prioritize relationships for psychic bonuses!"
        }
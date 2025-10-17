import json
from datetime import datetime

class FirebaseBridge:
    def __init__(self):
        self.battle_data = {}

    def save_progress(self, game):
        data = {
            "protagonist": {"name": game.protagonist.name, "morale": game.protagonist.morale},
            "base": {"pleb_morale": game.base.morale, "resources": game.base.resources},
            "technology": game.technology.tree,
            "timestamp": datetime.now().isoformat()
        }
        self.battle_data = data
        return json.dumps(data, indent=2)

    def load_lore(self):
        return {
            "lore": "Aurora Galaxy V20: Tactical Isekai with Advanced AI",
            "version": "20.0",
            "tip": "Prioritize relationships for psychic bonuses!"
        }
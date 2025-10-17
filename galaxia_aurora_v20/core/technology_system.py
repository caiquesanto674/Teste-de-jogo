from typing import Dict
from .base_system import MilitaryBase
from .character_system import Protagonist

import json

class TechnologySystem:
    def __init__(self, tree_path="galaxia_aurora_v20/assets/tech_tree.json"):
        self.tree = self._load_tree(tree_path)
        self.research_active = False

    def _load_tree(self, path: str) -> Dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Fallback to a default tree if file is missing or corrupt
            return {
                "Psi_Defense": {"level": 1, "bonus": 1.0, "cost": 9999},
                "Warfare_Attack": {"level": 1, "bonus": 1.0, "cost": 9999},
                "Production": {"level": 1, "bonus": 1.0, "cost": 9999}
            }

    def research(self, tech_type: str, resources: Dict) -> bool:
        tech = self.tree.get(tech_type)
        if resources.get("TechPoints", 0) >= tech["cost"]:
            resources["TechPoints"] -= tech["cost"]
            tech["level"] += 1
            tech["bonus"] += 0.2
            self.research_active = True
            return True
        return False

    def apply_bonuses(self, base: MilitaryBase, protagonist: Protagonist):
        if self.research_active:
            base.production_bonus = self.tree["Production"]["bonus"]
            base.defenses = self.tree["Psi_Defense"]["bonus"]
            protagonist.tech_bonus = self.tree["Warfare_Attack"]["bonus"]
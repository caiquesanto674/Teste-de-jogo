from .base_system import MilitaryBase
from .character_system import Protagonist

class TechnologySystem:
    def __init__(self):
        self.tree = {
            "Psi_Defense": {"level": 1, "bonus": 1.0, "cost": 100},
            "Warfare_Attack": {"level": 1, "bonus": 1.0, "cost": 150},
            "Production": {"level": 1, "bonus": 1.0, "cost": 75}
        }
        self.research_active = False

    def research(self, tech_type: str, resources) -> bool:
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
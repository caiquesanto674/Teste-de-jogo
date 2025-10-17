import logging
from .base_system import MilitaryBase

class EconomySystem:
    def __init__(self):
        self.base_rates = {
            "Metal": 100, "Energy": 50, "Food": 10,
            "Ether": 0.1, "TechPoints": 20
        }

    def calculate_factor(self, base: MilitaryBase) -> float:
        return max(0.25, base.pleb_morale / base.max_morale) * base.production_bonus

    def execute_production(self, base: MilitaryBase):
        factor = self.calculate_factor(base)
        base.produce_resources(factor)
        logging.info(f"💰 Economy: Factor {factor:.2f} | Production active")
from .base_system import MilitaryBase

class EconomySystem:
    def __init__(self):
        """Initializes resource production."""
        self.production_rates = {"Energy": 10, "Metal": 5, "Rare Food": 1, "Aether": 0}

    def generate_resources(self, base: MilitaryBase):
        """Generates resources based on the base's morale."""
        factor = max(0.25, base.morale / 100)
        for resource, value in self.production_rates.items():
            base.resources[resource] = base.resources.get(resource, 0) + int(value * factor)
        return "Production complete."
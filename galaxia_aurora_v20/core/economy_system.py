from .base_system import MilitaryBase

class Economy:
    def __init__(self):
        """Initializes resource production."""
        self.production = {"Energy": 10, "Metal": 5, "Rare Food": 1, "Aether": 0}

    def generate_resources(self, base: MilitaryBase):
        """Generates resources based on the base's morale."""
        factor = max(0.25, base.morale / 100)
        for resource, value in self.production.items():
            base.resources[resource] += int(value * factor)
        return "Production complete."
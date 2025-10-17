class MilitaryBase:
    def __init__(self, name: str = "Solaris Stronghold"):
        self.name = name
        self.level = 1
        self.pleb_morale = 75
        self.max_morale = 100
        self.resources = {
            "Metal": 1000, "Energy": 2000, "Food": 500,
            "Ether": 2, "TechPoints": 100
        }
        self.defenses = 1.0
        self.production_bonus = 1.0

    def apply_morale_impact(self, impact: int):
        self.pleb_morale = max(0, min(self.max_morale, self.pleb_morale + impact))

    def produce_resources(self, economy_factor: float):
        for resource, base in {"Metal": 100, "Energy": 50, "Food": 10}.items():
            production = int(base * economy_factor * self.production_bonus)
            self.resources[resource] += production
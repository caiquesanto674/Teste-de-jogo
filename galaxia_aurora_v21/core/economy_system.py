import random

class Economy:
    """
    [PT] Gerencia recursos, tecnologia, mercado.
    [EN] Manages resources, technology, and market.
    """

    def __init__(self):
        self.gold = 1200.0
        self.technology = 2.0  # Tech level
        self.prices = {"metal": 10.0, "energy": 15.0}

    def update_market(self):
        for resource in self.prices:
            factor = 1 + random.uniform(-0.05, 0.09) + self.technology / 100
            self.prices[resource] = max(
                1.0, round(self.prices[resource] * factor, 2)
            )

    def upgrade_technology(self, cost=100.0) -> bool:
        if self.gold >= cost:
            self.gold -= cost
            self.technology += 0.5
            print("[UPGRADE] Tech Improved/Tech Aprimorada")
            return True
        return False
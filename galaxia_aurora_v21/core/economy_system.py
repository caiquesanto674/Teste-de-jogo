import random

class Economy:
    def __init__(self):
        self.gold = 1200.0
        self.resources = {"metal": 10.0, "energy": 15.0}
        self.market_dynamics = {"metal": 0, "energy": 0}

    def update_market(self):
        for resource in self.resources:
            fluctuation = random.uniform(-0.05, 0.1)
            self.resources[resource] = max(1, round(self.resources[resource] * (1 + fluctuation), 2))

    def buy(self, resource: str, quantity: int) -> bool:
        total_cost = self.resources[resource] * quantity
        if self.gold >= total_cost:
            self.gold -= total_cost
            print(f"Bought {quantity} of {resource}.")
            return True
        print("Not enough gold!")
        return False
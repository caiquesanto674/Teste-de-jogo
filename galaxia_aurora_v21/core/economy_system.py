import random

class Economy:
    """Handles resources, market pricing, and technology upgrades."""
    def __init__(self):
        self.balance = 1200.0
        self.tech_level = 1.5
        self.market_prices = {'metal': 11.0, 'energy': 16.0, 'cryptocoin': 0.02}

    def update_market(self):
        for resource in self.market_prices:
            fluctuation = random.uniform(-0.04, 0.11) + (self.tech_level / 100)
            self.market_prices[resource] = max(1, round(self.market_prices[resource] * (1 + fluctuation), 2))

    def buy(self, item: str, quantity: int) -> bool:
        cost = self.market_prices.get(item, 0) * quantity
        if self.balance >= cost:
            self.balance -= cost
            print(f"Purchased: {quantity} {item}, cost: {cost:.2f}")
            return True
        print(f"Insufficient balance to buy {item}.")
        return False

    def upgrade_tech(self, investment=100) -> bool:
        if self.balance >= investment:
            self.balance -= investment
            self.tech_level += 0.5
            print(f"Technology upgraded! Current level: {self.tech_level:.2f}")
            return True
        print("Not enough funds to upgrade technology.")
        return False
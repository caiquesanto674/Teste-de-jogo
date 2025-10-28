import random
from typing import Dict

# =================== ECONOMY, TECHNOLOGY AND MARKET ===================

class Economy:
    """
    Manages the base's economy, including financial balance, technology level,
    and a resource market with dynamic prices.
    """
    def __init__(self):
        """Initializes the economy system."""
        self.balance: float = 1200.0
        self.tech: float = 1.5
        self.market: Dict[str, float] = {'metal': 11.0, 'energy': 16.0, 'cryptocurrency': 0.02}
        self.crypto: float = 0.02  # Support for crypto and future currencies

    def update(self):
        """
        Updates market prices based on random variation and the base's
        technology level.
        """
        for m in self.market:
            var = random.uniform(-0.04, 0.11) + (self.tech / 100)
            self.market[m] = max(1, round(self.market[m] * (1 + var), 2))

    def buy(self, item: str, qtd: int) -> bool:
        """
        Buys a quantity of an item from the market, if there is sufficient
        balance.

        Args:
            item: The item to be purchased.
            qtd: The quantity to be purchased.

        Returns:
            True if the purchase is successful, False otherwise.
        """
        val = self.market[item] * qtd
        if self.balance >= val:
            self.balance -= val
            print(f"Purchased: {qtd} {item}, cost: {val:.2f}")
            return True
        print(f"Insufficient balance for {item}.")
        return False

    def upgrade_tech(self, invest: int = 100) -> bool:
        """
        Upgrades the base's technology level, if there is sufficient
        balance for the investment.

        Args:
            invest: The amount to be invested in the upgrade.

        Returns:
            True if the upgrade is successful, False otherwise.
        """
        if self.balance >= invest:
            self.balance -= invest
            self.tech += 0.5
            print(f"Tech upgrade! Current level: {self.tech:.2f}")
            return True
        else:
            print("Insufficient investment.")
            return False
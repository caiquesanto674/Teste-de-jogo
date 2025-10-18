import datetime
import random
from typing import Dict, Any, List

class AIModule:
    """AI module for defense, narrative, and dynamic analysis."""
    def __init__(self, name: str):
        self.name = name
        self.version = 1.0
        self.log: List[str] = []

    def analyze(self, context: Dict[str, Any]):
        ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        analysis_result = "AI status normal."

        if self.name == "Market AI" and "economy" in context:
            metal_price = context["economy"].market_prices.get('metal', 100)
            if metal_price < 10.0:
                analysis_result = f"Market alert: Metal price is low (${metal_price}). Good time to buy."

        if self.name == "Defense/Tactics" and "characters" in context:
            for char in context["characters"]:
                # In a real scenario, Character would have health. We'll simulate it.
                if random.randint(1, 100) < 30: # Simulating a character is in low health
                    analysis_result = f"Tactical alert: {char.name}'s integrity is low. Recommend support."

        self.log.append(f"{ts}: [{self.name}] {analysis_result}")
        return analysis_result

    def auto_learn(self):
        if random.random() > 0.58:
            self.version += 0.01
            print(f"AI '{self.name}' upgraded: version {self.version:.2f}")
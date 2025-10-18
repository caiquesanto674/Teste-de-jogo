import random
from datetime import datetime
from typing import Dict, List, Any

class AIProtocol:
    """
    [PT] Protocolo IA: Evolução, verificação, narrativa e defesa.
    [EN] AI protocol: Evolution, self-check, storytelling and defense.
    """

    def __init__(self, name="AI Core"):
        self.name = name
        self.version = 1.0
        self.log: List[str] = []

    def analyze_context(self, context: Dict[str, Any]):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M')
        msg = "System Normal/Status IA normal" # Default message

        # Market AI Logic
        if self.name == "Market AI" and "economy" in context:
            economy = context["economy"]
            metal_price = economy.prices.get('metal', 100)
            if metal_price < 9.5 and economy.gold > 500:
                msg = f"Market Alert: Metal price is low (${metal_price}). AI suggests purchase."
                economy.purchase_resource("metal", 20)

        # Defense AI Logic
        if self.name == "Defense/Tactics" and "characters" in context:
            if any(char.role == "Inimigo" for char in context["characters"]):
                msg = "Threat Detected: Enemy unit present in the operational area."

        self.log.append(f"{ts}: [{self.name}] {msg}")

        # Evolutionary upgrade
        if random.random() > 0.58:
            self.version += 0.01
            self.log.append(f"{ts}: [{self.name}] AI upgraded to v{self.version:.2f}")

    def auto_learn(self):
        if random.random() > 0.58:
            self.version += 0.01
            print(f"AI '{self.name}' upgraded: version {self.version:.2f}")
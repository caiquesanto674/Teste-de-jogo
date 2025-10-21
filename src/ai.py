import random

class NPCCommander:
    def __init__(self, name, economy, base, ticker):
        self.name = name
        self.economy = economy
        self.base = base
        self.ticker = ticker
        self.peacefulness = random.randint(40, 60)
        self.focus = random.choice(["strategy", "technology", "attack"])

    def combat_action(self, target_base):
        """Tactical combat action using the unit with the highest Command or Force."""
        if not self.base.fleet:
            self.ticker.register("[NPC] No fleet for attack.")
            return

        # Selects the strongest unit or the one with the highest command for the mission
        attacking_unit = max(self.base.fleet, key=lambda u: u.force + u.command)

        # Choose a random ability
        if not attacking_unit.abilities:
            self.ticker.register(f"[NPC:{self.name}] {attacking_unit.name} no active abilities.")
            return

        ability_chosen = random.choice(attacking_unit.abilities)

        # The NPC consumes its own resources and attacks
        attacking_unit.execute_action(
            target=target_base,
            ability=ability_chosen,
            economy=self.economy,
            ticker=self.ticker
        )
        self.ticker.register(f"[NPC:{self.name}] Action executed: {ability_chosen.name} against {target_base.name}.")

    def evaluate_action(self, action, value=0):
        """Confirms and logs the NPC's behavioral phrase/response."""
        if action == "ATTACK":
            result = "REJECTED_INFERIOR_FORCE" if self.peacefulness > 70 else "CONFIRMED_COUNTER_ATTACK"
            phrase = "⚠️ Tactical retreat and request for reinforcements." if result.startswith("REJECTED") else "🔥 Prepare troops for emergency response!"
        elif action == "ALLY":
            result = "CONFIRMED_ALLIANCE" if self.peacefulness > 60 else "PENDING_NEGOTIATION"
            phrase = "🤝 Alliance accepted. Prepare logistical integration." if result.startswith("CONFIRMED") else "🕊️ Proposal under analysis."
        elif action == "RESEARCH":
            success = self.economy.invest_research(value, self.ticker)
            result = "CONFIRMED_RESEARCH" if success else "FAILED_RESEARCH"
            phrase = "📚 Scientific collaboration approved." if success else "⏳ Awaiting resources to start."
        else:
            result = "NEUTRAL"
            phrase = "🚦 Neutral state. Monitoring environment."
        self.ticker.register(f"[NPC:{self.name}] state:{result} - {phrase}")
        return result

from src.enums import ResourceType

class Resource:
    def __init__(self, type, quantity, rate):
        self.type = type
        self.quantity = quantity
        self.production_rate = rate
    def produce(self):
        self.quantity += self.production_rate

class Economy:
    def __init__(self):
        self.resources = {
            ResourceType.METAL: Resource(ResourceType.METAL, 500, 10),
            ResourceType.ENERGY: Resource(ResourceType.ENERGY, 300, 8),
            ResourceType.CREDITS: Resource(ResourceType.CREDITS, 1000, 20),
            ResourceType.RESEARCH: Resource(ResourceType.RESEARCH, 50, 2),
        }
        self.technologies = set()
        self.tech_level = 1.0

    def update(self, ticker):
        for r in self.resources.values():
            r.produce()
        ticker.register(f"[ECONOMY] Resources produced: {[f'{r.type.value}:{r.quantity:.1f}' for r in self.resources.values()]}")

    def invest_research(self, value, ticker):
        if self.resources[ResourceType.RESEARCH].quantity >= value:
            self.resources[ResourceType.RESEARCH].quantity -= value
            self.tech_level += 0.08
            ticker.register(f"[RESEARCH] Investment of {value} completed. Tech Level: {self.tech_level:.2f}")
            return True
        ticker.register(f"[RESEARCH] Failed due to lack of resources.")
        return False

    def consume_cost(self, cost):
        """Attempts to consume resources and returns True/False."""
        can_consume = True
        for type, value in cost.items():
            if self.resources[type].quantity < value:
                can_consume = False
                break

        if can_consume:
            for type, value in cost.items():
                self.resources[type].quantity -= value
            return True
        return False

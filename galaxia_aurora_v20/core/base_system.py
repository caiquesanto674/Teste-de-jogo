def clamp(value, min_value, max_value):
    """Clamps a value between a minimum and a maximum."""
    return max(min_value, min(value, max_value))

class MilitaryBase:
    def __init__(self, name="Solaris"):
        """Initializes the military base with a name and resources."""
        self.name = name
        self.level = 1
        self.resources = {"Energy": 100, "Metal": 20, "Rare Food": 2, "Aether": 1, "TechPoints": 100}
        self.morale = 80
        self.max_morale = 100
        self.production_bonus = 1.0
        self.defenses = 1.0

    def apply_morale_impact(self, impact):
        """Applies an impact to the base's morale."""
        self.morale = clamp(self.morale + impact, 0, self.max_morale)
        return f"Current morale: {self.morale}"
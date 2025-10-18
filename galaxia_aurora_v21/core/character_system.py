import uuid

class Character:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.id = uuid.uuid4().hex
        self.health = 100
        self.attack_power = 10

    def confirm_action(self) -> str:
        return f"[CONFIRM] {self.role.upper()} {self.name}: Action confirmed."

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health now: {self.health}")
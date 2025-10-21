import random
from src.enums import ResourceType, UnitType, MissionState

class DetailedAbility:
    """Defines complex abilities, including psychological powers and group effects."""
    def __init__(self, name, focused_unit_type, energy_cost, base_damage=0, moral_effect=0, group_effect_txt="None"):
        self.name = name
        self.focused_unit_type = focused_unit_type # UnitType that receives the buff (e.g., INFANTRY)
        self.energy_cost = energy_cost           # Cost to the Economy
        self.base_damage = base_damage           # Direct damage or impact
        self.moral_effect = moral_effect         # Impact on target/group morale
        self.group_effect_txt = group_effect_txt # Description of the group effect (e.g., Harem Battle)

class Unit:
    """Unit with detailed attributes, morale, and active/passive abilities."""
    def __init__(self, name, type, force, moral=100, command=0, abilities=None):
        self.name = name
        self.type = type
        self.force = force      # Base Damage / Brute Force
        self.moral = moral      # Resilience
        self.command = command  # Buff/Leadership Capacity
        self.abilities = abilities if abilities is not None else []
        self.hp = force * 5     # HP based on Force

    def display(self):
        return f"|{self.name} ({self.type.value})| F:{self.force} Mor:{self.moral:.1f} Cmd:{self.command} HP:{self.hp:.0f}|"

    def execute_action(self, target, ability, economy, ticker):
        """Executes the ability, consumes resources, and logs the detailed effect."""
        if not economy.consume_cost({ResourceType.ENERGY: ability.energy_cost}):
            ticker.register(f"[FAIL] {self.name} lacks Energy for {ability.name}.")
            return

        # Damage and Brute Force Logic (Força Bélica)
        final_damage = ability.base_damage + (self.force * random.uniform(0.8, 1.2))

        # Psychological Effect Logic (Poderes Psicológicos)
        if self.type == UnitType.PSYCHOLOGICAL:
            # Psychology: ignores armor and affects morale
            target.moral -= ability.moral_effect + (self.command * 0.5)
            final_damage *= 0.1 # Low physical damage
            ticker.register(f"🧠 {self.name} (Psi) used {ability.name}. {target.name}'s Moral dropped to {target.moral:.1f}.")

        # Command Effect Logic (Group Buff)
        elif self.command > 0 and ability.group_effect_txt != "None":
            # Command: buffs allies (simulation)
            for unit in target.fleet: # Target is the enemy Base in simulation
                if unit.type == ability.focused_unit_type:
                    unit.force += self.command * 0.1
                    unit.moral += self.command * 0.2
            ticker.register(f"🌟 {self.name} (Cmd) used {ability.name}. Command Tactics activated! {ability.group_effect_txt}.")
            return

        # Physical Damage Logic (Brute Force/Força Bélica)
        target.hp -= final_damage
        ticker.register(f"💥 {self.name} (B.Force) attacked {target.name}. Damage {final_damage:.1f}. HP remaining: {target.hp:.1f}.")

        # Low Morale Logic
        if target.moral <= 20 and target.hp > 0:
            target.force *= 0.5
            ticker.register(f"❌ {target.name} in panic state! Force reduced by half.")


class MilitaryBase:
    def __init__(self, name, initial_hp=1000):
        self.name = name
        self.fleet = []
        self.upgrades = []
        self.state = MissionState.NEUTRAL
        self.hp = initial_hp
        self.moral = 100 # Base Morale
        self.force = 0 # Placeholder for defense

    def add_unit(self, unit):
        self.fleet.append(unit)

    def status(self):
        return f"Base: {self.name} | Units: {len(self.fleet)} | HP: {self.hp:.1f} | State: {self.state.name}"

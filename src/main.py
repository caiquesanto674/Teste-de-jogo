import random
import json
from src.enums import UnitType
from src.systems import Ticker, World
from src.economy import Economy
from src.entities import MilitaryBase, Unit, DetailedAbility
from src.ai import NPCCommander

# ===========================
# DATA LOADING
# ===========================
def load_abilities():
    with open('assets/abilities.json', 'r') as f:
        return json.load(f)

def load_units():
    with open('assets/units.json', 'r') as f:
        return json.load(f)

# ===========================
# MAIN GAME CYCLE
# ===========================
def game_cycle(ticks=5):
    ticker = Ticker()
    world = World()
    eco_player = Economy()
    base_player = MilitaryBase("Caíque Fortress")

    eco_npc = Economy()
    base_npc = MilitaryBase("Shadow Outpost")
    npc = NPCCommander("Lord Enygma", eco_npc, base_npc, ticker)

    # --- Load Game Data ---
    abilities_data = load_abilities()
    units_data = load_units()

    # --- Create Abilities ---
    player_abilities = {a['name']: DetailedAbility(a['name'], UnitType[a['focused_unit_type']], a['energy_cost'], a['base_damage'], a['moral_effect'], a['group_effect_txt']) for a in abilities_data['player_abilities']}
    npc_abilities = {a['name']: DetailedAbility(a['name'], UnitType[a['focused_unit_type']], a['energy_cost'], a['base_damage'], a['moral_effect'], a['group_effect_txt']) for a in abilities_data['npc_abilities']}
    all_abilities = {**player_abilities, **npc_abilities}

    # --- Create Units ---
    for unit_data in units_data['player_units']:
        unit_abilities = [all_abilities[ability_name] for ability_name in unit_data.get('abilities', [])]
        base_player.add_unit(Unit(unit_data['name'], UnitType[unit_data['type']], unit_data['force'], unit_data.get('moral', 100), unit_data.get('command', 0), unit_abilities))

    for unit_data in units_data['npc_units']:
        unit_abilities = [all_abilities[ability_name] for ability_name in unit_data.get('abilities', [])]
        base_npc.add_unit(Unit(unit_data['name'], UnitType[unit_data['type']], unit_data['force'], unit_data.get('moral', 100), unit_data.get('command', 0), unit_abilities))

    # --- Main Game Cycle ---
    for tick in range(ticks):
        ticker.register(f"\n=== TICK {tick} - {base_player.name} vs {base_npc.name} ===")
        world.run_event(ticker)

        # Player Action (Simulation: Focus on Economy and Research)
        eco_player.update(ticker)
        eco_player.invest_research(random.randint(5, 15), ticker)

        # NPC Action (Focus on Advanced Tactical Combat)
        eco_npc.update(ticker)
        npc.combat_action(base_player) # The NPC attacks the player's base

        # Round Summary
        ticker.register(base_player.status())
        ticker.register(f"Main Unit Status (Player): {base_player.fleet[0].display()}")
        ticker.show()

    print("\n--- END OF ADVANCED SIMULATION CYCLE ---")
    print("FINAL REPORT:")
    ticker.show()

# Execution Example
if __name__ == "__main__":
    game_cycle(5)

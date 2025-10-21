import unittest
from src.economy import Economy
from src.entities import Unit, DetailedAbility
from src.enums import ResourceType, UnitType
from src.systems import Ticker

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.ticker = Ticker()
        self.economy = Economy()

    def test_resource_production(self):
        initial_metal = self.economy.resources[ResourceType.METAL].quantity
        self.economy.update(self.ticker)
        self.assertGreater(self.economy.resources[ResourceType.METAL].quantity, initial_metal)

    def test_insufficient_funds_for_research(self):
        initial_research = self.economy.resources[ResourceType.RESEARCH].quantity
        self.economy.resources[ResourceType.RESEARCH].quantity = 10
        self.assertFalse(self.economy.invest_research(20, self.ticker))
        self.assertEqual(self.economy.resources[ResourceType.RESEARCH].quantity, 10)

    def test_unit_creation(self):
        unit = Unit("Test Unit", UnitType.INFANTRY, 100)
        self.assertEqual(unit.name, "Test Unit")
        self.assertEqual(unit.hp, 500)

    def test_unit_action_consumption(self):
        unit = Unit("Test Unit", UnitType.INFANTRY, 100)
        target = Unit("Target", UnitType.ARMORED, 150)
        ability = DetailedAbility("Test Ability", UnitType.INFANTRY, 50, 20)

        initial_energy = self.economy.resources[ResourceType.ENERGY].quantity
        unit.execute_action(target, ability, self.economy, self.ticker)
        self.assertEqual(self.economy.resources[ResourceType.ENERGY].quantity, initial_energy - 50)
        self.assertLess(target.hp, target.force * 5)

if __name__ == '__main__':
    unittest.main()

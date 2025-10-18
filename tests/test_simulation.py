import unittest
from src.services import StorageService
from src.economy import Economy
from src.protocols import PowerProtocol, AIProtocol
from src.entities import Character
from src.metrics import MetricXValidator
from src.simulation import MilitaryBase

class TestSimulation(unittest.TestCase):

    def test_storage_service(self):
        """Testa o serviço de armazenamento."""
        storage = StorageService()
        storage.save("test_key", "test_value")
        self.assertEqual(storage.data["test_key"], "test_value")
        storage.sync()
        self.assertIn("Cloud Sync", storage.log[0])

    def test_economy(self):
        """Testa o sistema de economia."""
        economy = Economy()
        initial_gold = economy.gold
        economy.upgrade_technology()
        self.assertLess(economy.gold, initial_gold)
        initial_prices = economy.prices.copy()
        economy.update_market()
        self.assertNotEqual(initial_prices, economy.prices)

    def test_power_protocol(self):
        """Testa o protocolo de poder."""
        power = PowerProtocol("Comandante")
        self.assertIn("Poder Psicológico", power.abilities)
        self.assertEqual(power.force_level, 1000)

    def test_ai_protocol(self):
        """Testa o protocolo de IA."""
        ai = AIProtocol()
        initial_version = ai.version
        ai.evolve_and_verify()
        self.assertGreaterEqual(ai.version, initial_version)

    def test_character(self):
        """Testa a criação de personagens."""
        char = Character("Test Character", "Test Role")
        self.assertEqual(char.name, "Test Character")
        self.assertIsNotNone(char.id)
        self.assertIn("Poder Psicológico", char.powers.abilities)

    def test_metric_x_validator(self):
        """Testa o validador de métricas."""
        metrics = MetricXValidator()
        impact, latency, data_share = metrics.validate(0.9)
        self.assertIsInstance(impact, float)
        self.assertIsInstance(latency, float)
        self.assertTrue(data_share)

    def test_military_base(self):
        """Testa a classe da base militar."""
        base = MilitaryBase("Test Base")
        base.add_character("Test Commander", "Comandante")
        self.assertEqual(len(base.characters), 1)
        initial_gold = base.economy.gold
        # Force an upgrade for a deterministic test
        base.economy.gold = 1000
        base.cycle()
        self.assertLess(base.economy.gold, initial_gold)

if __name__ == '__main__':
    unittest.main()
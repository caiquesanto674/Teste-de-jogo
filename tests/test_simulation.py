import unittest
from src.core import MilitaryBase, Resource
from src.economy import Economy, Technology
from src.ai import AIProtocol
from src.entities import Character

class TestSimulation(unittest.TestCase):

    def setUp(self):
        """Configura os componentes para cada teste."""
        self.base = MilitaryBase()
        self.technology = Technology()
        self.available_resources = [Resource("Éter", 50.0)]
        self.economy = Economy(self.base, self.technology)
        self.ai_protocol = AIProtocol(self.economy, self.available_resources)

    def test_add_soldier(self):
        """Testa a adição de um soldado à base."""
        initial_morale = self.base.morale
        soldier = Character("Test Soldier")
        self.base.add_soldier(soldier)
        self.assertEqual(len(self.base.soldiers), 1)
        self.assertEqual(self.base.soldiers[0], soldier)
        self.assertEqual(self.base.morale, initial_morale + 5)

    def test_upgrade_technology(self):
        """Testa o upgrade de tecnologia."""
        initial_level = self.technology.level
        self.base.resources = 300
        self.economy.upgrade_technology(200)
        self.assertEqual(self.technology.level, initial_level + 0.5)
        self.assertEqual(self.base.resources, 100)

    def test_purchase_resource(self):
        """Testa a compra de recursos."""
        ether = self.available_resources[0]
        self.base.resources = 600
        self.economy.purchase_resource(ether, 10)
        self.assertEqual(self.base.inventory["Éter"].quantity, 10)
        self.assertEqual(self.base.resources, 100)

    def test_ai_analysis(self):
        """Testa a análise e execução da IA."""
        self.base.resources = 900
        self.ai_protocol.analyze_and_execute()
        self.assertIn("Éter", self.base.inventory)
        self.assertEqual(self.base.inventory["Éter"].quantity, 10)
        self.assertEqual(self.base.resources, 400)

    def test_character_action_confirmation(self):
        """Testa a confirmação de ação do personagem."""
        character = Character("Test Character", volicao_level=50)
        # Este teste apenas verifica se a função não gera erro.
        # A verificação da saída é mais adequada para testes de integração.
        try:
            character.confirm_action("Test Action")
        except Exception as e:
            self.fail(f"confirm_action() gerou uma exceção: {e}")

if __name__ == '__main__':
    unittest.main()
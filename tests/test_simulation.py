import unittest
from src.economy import Economy
from src.simulation import AIModule, Character, ChatLog, MilitaryBase
from src.security import AuthManager, CryptoChat, SecureBackup

class TestSimulation(unittest.TestCase):

    def setUp(self):
        """Configura a simulação para cada teste."""
        self.auth = AuthManager()
        self.chat = CryptoChat(key="testkey")
        self.backup = SecureBackup(key="backupkey")
        self.econ = Economy()
        self.chat_log = ChatLog()
        self.ia_stack = [AIModule("TestAI")]
        self.base = MilitaryBase("TestBase", self.auth, self.chat, self.econ, self.backup, self.ia_stack, self.chat_log)

    def test_economy_update(self):
        """Testa a atualização do mercado na economia."""
        initial_market = self.econ.market.copy()
        self.econ.update()
        self.assertNotEqual(initial_market, self.econ.market)

    def test_economy_buy(self):
        """Testa a função de compra na economia."""
        initial_balance = self.econ.balance
        self.econ.buy("metal", 10)
        self.assertLess(self.econ.balance, initial_balance)

    def test_add_character(self):
        """Testa a adição de um novo personagem à base."""
        self.base.add_personagem("TestCharacter", "TestRole")
        self.assertEqual(len(self.base.personagens), 1)
        self.assertEqual(self.base.personagens[0].name, "TestCharacter")

    def test_simulation_cycle(self):
        """Testa se o ciclo de simulação é executado sem erros."""
        try:
            self.base.ciclo()
        except Exception as e:
            self.fail(f"O ciclo da simulação gerou uma exceção: {e}")

    def test_character_falar_no_leak(self):
        """Testa se o método falar do Character não vaza o código de confirmação."""
        char = Character("TestLeak", "Spy")
        # Executa o método falar várias vezes para garantir a robustez do teste
        for _ in range(50):
            phrase = char.falar()
            self.assertNotIn(char.confirm_code, phrase, "O código de confirmação foi vazado em uma frase.")

if __name__ == '__main__':
    unittest.main()
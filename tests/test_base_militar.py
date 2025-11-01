import unittest
from src.game.base_militar import BaseMilitar
from src.game.unidade_militar import Soldado, Oficial

class TestBaseMilitar(unittest.TestCase):
    def setUp(self):
        self.base = BaseMilitar()
        self.sd = Soldado("João", "Soldado")
        self.of = Oficial("Maria", "Tenente")

    def test_adicionar_unidade(self):
        self.base.adicionar_unidade(self.sd)
        self.assertEqual(len(self.base.unidades), 1)
        self.assertIn(f"{self.sd.nome} ({self.sd.patente}) foi integrado à base.", self.base.evento_log)

    def test_consumir_recursos(self):
        self.assertEqual(self.base.economia.consumir("comida", 20), "20 unidades de comida consumidas.")
        self.assertEqual(self.base.economia.recursos["comida"], 80)

    def test_produzir_recursos(self):
        self.assertEqual(self.base.economia.produzir("combustível", 10), "10 unidades de combustível produzidas.")
        self.assertEqual(self.base.economia.recursos["combustível"], 60)

    def test_find_and_fix_bug(self):
        self.base.economia.recursos["munição"] = -10
        self.base.find_and_fix_bug()
        self.assertEqual(self.base.economia.recursos["munição"], 0)
        self.assertIn("Bug corrigido: recurso munição negativo, redefinido para 0.", self.base.evento_log)

if __name__ == '__main__':
    unittest.main()

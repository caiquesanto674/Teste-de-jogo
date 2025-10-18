import unittest
from src.economy import Economia, BaseMilitar

class TestEconomy(unittest.TestCase):

    def test_gerar_recursos(self):
        """Testa se a geração de recursos funciona corretamente."""
        economia = Economia()
        base = BaseMilitar()
        base.moral = 100
        economia.gerar(base)
        self.assertEqual(base.recursos["Energia"], 110)
        self.assertEqual(base.recursos["Metal"], 25)
        self.assertEqual(base.recursos["Comida Rara"], 3)

    def test_aplicar_impacto_moral(self):
        """Testa se o impacto na moral é aplicado corretamente."""
        base = BaseMilitar()
        base.aplicar_impacto(10)
        self.assertEqual(base.moral, 90)
        base.aplicar_impacto(-20)
        self.assertEqual(base.moral, 70)

    def test_clamp_moral(self):
        """Testa se a moral da base é restringida aos limites."""
        base = BaseMilitar()
        base.aplicar_impacto(30)
        self.assertEqual(base.moral, 100)
        base.aplicar_impacto(-120)
        self.assertEqual(base.moral, 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.units import UnidadeMilitar, UnidadeSuporte
from src.agent import AgentePPO
from src.actions import ActionType
from src.economy import BaseMilitar

class TestUnits(unittest.TestCase):

    def setUp(self):
        """Configura as unidades para cada teste."""
        self.agente_comandante = AgentePPO()
        self.agente_inimigo = AgentePPO()
        self.base = BaseMilitar()
        self.comandante = UnidadeMilitar("Comandante", 20, 100, self.agente_comandante)
        self.inimigo = UnidadeMilitar("Inimigo", 30, 100, self.agente_inimigo)
        self.suporte = UnidadeSuporte("Suporte", 5, 50, AgentePPO())

    def test_take_damage(self):
        """Testa se a unidade sofre dano corretamente."""
        self.comandante.take_damage(20)
        self.assertEqual(self.comandante.hp, 80)
        self.comandante.take_damage(90)
        self.assertEqual(self.comandante.hp, 0)

    def test_cura_suporte(self):
        """Testa se a unidade de suporte cura corretamente."""
        self.comandante.hp = 60
        self.suporte.acao(self.comandante, None)
        self.assertEqual(self.comandante.hp, 80)

    def test_acao_atacar(self):
        """Testa se a ação de atacar é selecionada e executada."""
        self.base.recursos["Éter"] = 0
        self.comandante.acao(self.inimigo, self.suporte, self.base)
        self.assertEqual(self.inimigo.hp, 80)

    def test_acao_atacar_especial(self):
        """Testa o ataque especial com Éter."""
        self.base.recursos["Éter"] = 1
        self.comandante.acao(self.inimigo, self.suporte, self.base)
        self.assertEqual(self.inimigo.hp, 40)
        self.assertEqual(self.base.recursos["Éter"], 0)

    def test_acao_recuar(self):
        """Testa se a ação de recuar é selecionada."""
        self.base.recursos["Éter"] = 0
        self.comandante.hp = 10
        acao = self.comandante.acao(self.inimigo, self.suporte, self.base)
        self.assertIn("recua", acao)

    def test_acao_buscar_suporte(self):
        """Testa se a ação de buscar suporte é selecionada."""
        self.base.recursos["Éter"] = 0
        self.comandante.hp = 40
        acao = self.comandante.acao(self.inimigo, self.suporte, self.base)
        self.assertIn("cura", acao)
        self.assertEqual(self.comandante.hp, 70)

if __name__ == '__main__':
    unittest.main()
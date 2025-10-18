import random

# ==================== MÓDULO 2: ECONOMIA E TECNologia (IA OTIMIZADA) ====================
class Economy:
    """
    Gerencia a economia do jogo, incluindo ouro, nível de tecnologia e preços
    de mercado para vários recursos.
    """
    def __init__(self):
        """Inicializa o sistema de economia."""
        self.gold = 1500.0
        self.technology = 4.0  # Nível Avançado (V4.0)
        self.prices = {"metal": 12.0, "energy": 18.0, "ether": 50.0}

    def update_market(self):
        """
        Atualiza os preços do mercado com base na volatilidade do mercado e na
        influência da tecnologia.
        """
        tech_influence = self.technology / 80 # Maior estabilidade
        for resource in self.prices:
            factor = 1 + random.uniform(-0.03, 0.06) + tech_influence
            self.prices[resource] = max(1.0, round(self.prices[resource] * factor, 2))

    def upgrade_technology(self, cost: float = 150.0) -> bool:
        """
        Faz o upgrade do nível de tecnologia se houver ouro suficiente.

        Args:
            cost: O custo do upgrade de tecnologia.

        Returns:
            True se o upgrade for bem-sucedido, False caso contrário.
        """
        if self.gold >= cost:
            self.gold -= cost
            self.technology += 0.75 # Aumento significativo
            return True
        return False
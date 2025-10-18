import random
from typing import Dict

# =================== ECONOMIA, TECNOLOGIA E MERCADO ===================

class Economy:
    """
    Gerencia a economia da base, incluindo balanço financeiro, nível tecnológico,
    e um mercado de recursos com preços dinâmicos.
    """
    def __init__(self):
        """Inicializa o sistema de economia."""
        self.balance: float = 1200.0
        self.tech: float = 1.5
        self.market: Dict[str, float] = {'metal': 11.0, 'energia': 16.0, 'criptomoeda': 0.02}
        self.crypto: float = 0.02  # Suporte cripto e moedas futuras

    def update(self):
        """
        Atualiza os preços do mercado com base em uma variação aleatória e no
        nível de tecnologia da base.
        """
        for m in self.market:
            var = random.uniform(-0.04, 0.11) + (self.tech / 100)
            self.market[m] = max(1, round(self.market[m] * (1 + var), 2))

    def buy(self, item: str, qtd: int) -> bool:
        """
        Compra uma quantidade de um item do mercado, se houver saldo suficiente.

        Args:
            item: O item a ser comprado.
            qtd: A quantidade a ser comprada.

        Returns:
            True se a compra for bem-sucedida, False caso contrário.
        """
        val = self.market[item] * qtd
        if self.balance >= val:
            self.balance -= val
            print(f"Comprado: {qtd} {item}, custo: {val:.2f}")
            return True
        print(f"Saldo insuficiente para {item}.")
        return False

    def upgrade_tech(self, invest: int = 100) -> bool:
        """
        Realiza um upgrade no nível de tecnologia da base, se houver saldo
        suficiente para o investimento.

        Args:
            invest: O valor a ser investido no upgrade.

        Returns:
            True se o upgrade for bem-sucedido, False caso contrário.
        """
        if self.balance >= invest:
            self.balance -= invest
            self.tech += 0.5
            print(f"Tech upgrade! Nível atual: {self.tech:.2f}")
            return True
        else:
            print("Investimento insuficiente.")
            return False
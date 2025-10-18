from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core import MilitaryBase, Resource

# ==================== MÓDULO 2: ECONOMIA E TECNOLOGIA (Tycoon) ====================
class Technology:
    """
    Gerencia o nível de tecnologia da base.
    """
    def __init__(self):
        """Inicializa o sistema de tecnologia."""
        self.level: float = 1.0

    def upgrade(self):
        """Aumenta o nível de tecnologia."""
        self.level += 0.5
        print(f"[TECH UPGRADE]: Nível de tecnologia atualizado para {self.level:.1f}.")

class Economy:
    """
    Gerencia as operações econômicas da base, como a compra de recursos e
    upgrades de tecnologia.
    """
    def __init__(self, base: MilitaryBase, tech: Technology):
        """
        Inicializa o sistema de economia.

        Args:
            base: A instância da base militar.
            tech: A instância do sistema de tecnologia.
        """
        self.base = base
        self.tech = tech

    def upgrade_technology(self, cost: float):
        """
        Tenta fazer o upgrade da tecnologia, se houver recursos suficientes.

        Args:
            cost: O custo do upgrade.
        """
        if self.base.resources >= cost:
            self.base.resources -= cost
            self.tech.upgrade()
        else:
            print("[ERRO TYCOON]: Capital insuficiente para upgrade.")

    def purchase_resource(self, resource: Resource, amount: int):
        """
        Tenta comprar uma quantidade de um recurso, se houver recursos suficientes.

        Args:
            resource: O recurso a ser comprado.
            amount: A quantidade a ser comprada.
        """
        cost = resource.price * amount
        if self.base.resources >= cost:
            self.base.resources -= cost
            self.base.add_to_inventory(resource, amount)
            print(f"[AQUISIÇÃO ESTRATÉGICA]: {amount} unidades de {resource.name} compradas. Custo: {cost:.2f} Ouro.")
            return True
        else:
            print("[ERRO ESTRATÉGICO]: Capital insuficiente para aquisição.")
            return False
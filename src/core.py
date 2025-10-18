from typing import List, Dict
from src.entities import Character

class Resource:
    """
    Representa um recurso no jogo, com um nome, preço e quantidade.
    """
    def __init__(self, name: str, price: float):
        """
        Inicializa um novo recurso.

        Args:
            name: O nome do recurso.
            price: O preço do recurso.
        """
        self.name: str = name
        self.price: float = price
        self.quantity: int = 0

# ==================== MÓDULO 1: CORE - BASE MILITAR ====================
class MilitaryBase:
    """
    A classe principal que representa a base militar e gerencia seus recursos,
    soldados e moral.
    """
    def __init__(self):
        """Inicializa a base militar."""
        self.soldiers: List[Character] = []
        self.resources: float = 1000.0
        self.morale: int = 100
        self.inventory: Dict[str, Resource] = {}
        print("[NEXUS CORE]: Base Militar inicializada.")

    def add_soldier(self, soldier: Character):
        """
        Adiciona um novo soldado à base e aumenta a moral.

        Args:
            soldier: O soldado a ser adicionado.
        """
        self.soldiers.append(soldier)
        self.morale += 5
        print(f"[AGENTE OP]: {soldier.name} adicionado (Moral: +5).")

    def add_to_inventory(self, resource: Resource, amount: int):
        """
        Adiciona uma quantidade de um recurso ao inventário da base.

        Args:
            resource: O recurso a ser adicionado.
            amount: A quantidade a ser adicionada.
        """
        if resource.name in self.inventory:
            self.inventory[resource.name].quantity += amount
        else:
            new_resource = Resource(resource.name, resource.price)
            new_resource.quantity = amount
            self.inventory[resource.name] = new_resource

    def display_status(self):
        """Exibe o status atual da base militar."""
        print(f"\n--- STATUS OPERACIONAL DO CORE NEXUS ---")
        print(f"Capital Fiduciário (Ouro): {self.resources:.2f}")
        print(f"Moral da Base (Volição): {self.morale}")
        print(f"Número de Agentes (OP): {len(self.soldiers)}")
        for name, resource in self.inventory.items():
            print(f"  > Recurso {name}: {resource.quantity} unidades.")
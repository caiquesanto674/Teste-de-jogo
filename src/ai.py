from src.economy import Economy
from src.core import Resource
from typing import List

# ==================== MÓDULO 3: AI PROTOCOL (Automação de Decisão) ====================
class AIProtocol:
    """
    Implementa um protocolo de IA que pode analisar o estado do jogo e tomar
    decisões de forma autônoma, como a compra de recursos.
    """
    def __init__(self, economy: Economy, available_resources: List[Resource]):
        """
        Inicializa o protocolo de IA.

        Args:
            economy: A instância do sistema de economia.
            available_resources: Uma lista de recursos disponíveis no jogo.
        """
        self.economy = economy
        self.available_resources = available_resources

    def analyze_and_execute(self):
        """
        Analisa o estado atual da economia e decide se deve comprar recursos
        de forma autônoma.
        """
        if self.economy.base.resources > 800:
            amount_to_buy = 10
            ether_resource = next((r for r in self.available_resources if r.name == "Éter"), None)
            if ether_resource:
                print("[ANÁLISE TYCOON]: Recursos adequados. Iniciando aquisição automática de Éter.")
                self.economy.purchase_resource(ether_resource, amount_to_buy)
        else:
            print("[ANÁLISE TYCOON]: Capital abaixo do limite de aquisição.")
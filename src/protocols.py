import random
from datetime import datetime
from typing import Dict, List

# ==================== MÓDULO 3: PROTOCOLO DE FORÇA E HABILIDADES ====================
class PowerProtocol:
    """
    Define e gerencia os níveis de poder e habilidades para diferentes papéis
    de personagens no jogo.
    """
    def __init__(self, role: str, initial_level: int = 1000):
        """
        Inicializa o protocolo de poder para um determinado papel.

        Args:
            role: O papel do personagem (ex: 'Comandante', 'Aliada').
            initial_level: O nível de força inicial.
        """
        self.role = role
        self.force_level = initial_level
        self.abilities = self._set_abilities()

    def _set_abilities(self) -> Dict[str, str]:
        """
        Define as habilidades de um personagem com base em seu papel.

        Returns:
            Um dicionário de habilidades.
        """
        if "Comandante" in self.role or "Protagonista" in self.role:
            return {
                "Poder Psicológico": "Controle de Vontade (Volição)",
                "Força Bélica": "Arsenal de Éter e Defesa Quântica",
                "Habilidade Especial": "Habilidade Harem: Sinergia de Moral"
            }
        elif "Aliada" in self.role:
            return {
                "Poder Psicológico": "Defesa Mental e Empatia Tática",
                "Força Bélica": "Suporte e Buff de Combate",
            }
        else: # Inimigo
             return {
                "Poder Psicológico": "Dano Moral e Corrupção Sideral",
                "Força Bélica": "Táticas de Invasão e Destruição",
            }

# ==================== MÓDULO 4: INTELIGÊNCIA ARTIFICIAL (V5.0) ====================
class AIProtocol:
    """
    Simula um protocolo de IA avançado que evolui e se auto-verifica ao
    longo do tempo.
    """
    def __init__(self):
        """Inicializa o protocolo de IA."""
        self.version = 5.0
        self.log: List[str] = []

    def evolve_and_verify(self):
        """
        Simula o processo de evolução da IA, com uma chance de aumentar o
        número da versão e registrar o evento.
        """
        if random.random() > 0.45: # Alta taxa de evolução
            self.version = round(self.version + 0.01, 2)
            self.log.append(f"{datetime.now().strftime('%H:%M:%S')}: CODE_OPTIMIZATION_SUCCESS - AI_V{self.version:.2f}. Novo código verificado.")
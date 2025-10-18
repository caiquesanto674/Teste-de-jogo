from datetime import datetime
from typing import Dict, List, Any

# ==================== MÓDULO 1: ARMAZENAMENTO E CLOUD (24H) ====================
class StorageService:
    """
    Simula um serviço de armazenamento em nuvem para persistência de dados,
    com suporte para sincronização periódica.
    """
    def __init__(self, provider: str = 'Azure-Google'):
        """
        Inicializa o serviço de armazenamento.

        Args:
            provider: O nome do provedor de nuvem (ex: 'Azure-Google').
        """
        self.provider = provider
        self.data: Dict[str, Any] = {}
        self.log: List[str] = []

    def save(self, key: str, value: Any):
        """
        Salva um par chave-valor no armazenamento de dados.

        Args:
            key: A chave para o dado.
            value: O dado a ser armazenado.
        """
        self.data[key] = value

    def sync(self):
        """
        Simula o processo de sincronização com a nuvem, registrando o evento
        em um log.
        """
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.log.append(f"[{timestamp}] Cloud Sync: {len(self.data)} chaves armazenadas.")
        print(f"[{self.provider}] Sincronização Cloud Concluída ({len(self.data)} chaves)")
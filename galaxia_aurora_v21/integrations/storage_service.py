from typing import Dict, Any

class StorageService:
    """[PT] Camada de persistência. [EN] Storage/persistence layer."""

    def __init__(self, provider='Azure-Google'):
        self.provider = provider
        self.data: Dict[str, Any] = {}

    def save(self, key: str, value: Any):
        self.data[key] = value
        print(f"[{self.provider}] SAVED/ARMAZENADO: {key}")

    def load(self, key: str) -> Any:
        return self.data.get(key)

    def sync(self):
        print(
            f"[{self.provider}] Cloud Sync ({len(self.data)} keys/chaves armazenadas)"
        )
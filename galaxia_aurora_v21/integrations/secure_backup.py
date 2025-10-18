import json
import hashlib
from ..core.security_system import CryptoSystem
from .cloud_storage import CloudStorage

class SecureBackup:
    def __init__(self, storage: CloudStorage):
        self.storage = storage
        self.crypto = CryptoSystem()

    def backup(self, key: str, data: str):
        """Hashes and stores data securely."""
        data_hash = str(hashlib.sha256(data.encode()).hexdigest())
        # In a real scenario, we might encrypt the data itself, not just the hash
        self.storage.save(key, data_hash)
        print(f"Secure backup stored for: {key}")

    def restore(self, key: str) -> str:
        """Restores a backup from storage."""
        return self.storage.load(key)
import json
import hashlib
from ..core.security_system import CryptoSystem
from .storage_service import StorageService

class SecureBackup:
    def __init__(self, storage: StorageService):
        self.storage = storage
        self.crypto = CryptoSystem()

    def backup(self, key: str, data: dict):
        """Encrypts and saves the game state to cloud storage."""
        # Serialize game state to a JSON string
        game_state_str = json.dumps(data)

        # Encrypt the data
        encrypted_data = self.crypto.encrypt(game_state_str)

        # Save to cloud storage
        self.storage.save(key, encrypted_data)
        print(f"Secure backup '{key}' created successfully.")

    def load_backup(self, key: str) -> dict:
        """Loads and decrypts a backup from cloud storage."""
        encrypted_data = self.storage.load(key)
        if encrypted_data:
            decrypted_str = self.crypto.decrypt(encrypted_data)
            return json.loads(decrypted_str)
        return None
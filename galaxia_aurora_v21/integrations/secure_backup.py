import json
from ..core.security_system import CryptoSystem
from .cloud_storage import CloudStorage

class SecureBackup:
    def __init__(self, storage: CloudStorage):
        self.storage = storage
        self.crypto = CryptoSystem()

    def create_backup(self, game_state: dict, backup_name: str):
        """Encrypts and saves the game state to cloud storage."""
        # Serialize game state to a JSON string
        game_state_str = json.dumps(game_state)

        # Encrypt the data
        encrypted_data = self.crypto.encrypt(game_state_str)

        # Save to cloud storage
        self.storage.save(backup_name, encrypted_data)
        print(f"Secure backup '{backup_name}' created successfully.")

    def load_backup(self, backup_name: str) -> dict:
        """Loads and decrypts a backup from cloud storage."""
        encrypted_data = self.storage.load(backup_name)
        if encrypted_data:
            decrypted_str = self.crypto.decrypt(encrypted_data)
            return json.loads(decrypted_str)
        return None
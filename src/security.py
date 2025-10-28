import uuid
import hashlib
import random
from typing import Dict, Any

# =================== SECURITY AND AUTHENTICATION ===================

class AuthManager:
    """
    Manages user registration and authentication using a salted password and
    a multi-factor authentication (MFA) code.
    """
    def __init__(self):
        """Initializes the authentication manager."""
        self.users: Dict[str, Dict[str, str]] = {}

    def register(self, login: str, password: str) -> str:
        """
        Registers a new user with a salt and password hash and generates an MFA code.

        Args:
            login: The username for registration.
            password: The password for the new user.

        Returns:
            The MFA code generated for the user.
        """
        salt = uuid.uuid4().hex
        pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        mfa_code = str(random.randint(100000, 999999))
        self.users[login] = {"salt": salt, "hash": pwd_hash, "mfa_code": mfa_code}
        print(f"User {login} registered. MFA code has been generated.")
        return mfa_code

    def authenticate(self, login: str, password: str, code: str) -> bool:
        """
        Authenticates a user by verifying the password hash and MFA code.

        Args:
            login: The username to authenticate.
            password: The password to verify.
            code: The MFA code to verify.

        Returns:
            True if authentication is successful, False otherwise.
        """
        user = self.users.get(login)
        if not user: return False
        hash_check = hashlib.sha256((password + user['salt']).encode()).hexdigest()
        return hash_check == user["hash"] and code == user["mfa_code"]

# =================== BASIC ENCRYPTION (MESSAGES) ===================

class CryptoChat:
    """
    Simulates an end-to-end encrypted chat system using a simple symmetric key.
    """
    def __init__(self, key: str):
        """
        Initializes CryptoChat with an encryption key.

        Args:
            key: The secret key to be used for encryption and decryption.
        """
        if not key:
            raise ValueError("The encryption key cannot be empty.")
        self.key = key

    def encrypt(self, msg: str) -> str:
        """
        Encrypts a message using the instance's key.

        Args:
            msg: The message to be encrypted.

        Returns:
            The encrypted message.
        """
        return ''.join(chr((ord(c) + len(self.key)) % 256) for c in msg)

    def decrypt(self, enc: str) -> str:
        """
        Decrypts a message using the instance's key.

        Args:
            enc: The encrypted message.

        Returns:
            The original message.
        """
        return ''.join(chr((ord(c) - len(self.key)) % 256) for c in enc)

    def enviar(self, user_from: str, user_to: str, msg: str) -> str:
        """
        Encrypts and sends a message to another user.

        Args:
            user_from: The sender of the message.
            user_to: The recipient of the message.
            msg: The message to be sent.

        Returns:
            The encrypted message.
        """
        enc = self.encrypt(msg)
        print(f"> [{user_from} -> {user_to}] (encrypted): {enc}")
        return enc

    def receber(self, enc: str) -> str:
        """
        Receives and decrypts a message.

        Args:
            enc: The encrypted message received.

        Returns:
            The original message.
        """
        dec = self.decrypt(enc)
        print(f"Received message: {dec}")
        return dec

# =================== ENCRYPTED BACKUP AND LOG ===================

class SecureBackup:
    """
    Manages data backup and restoration using symmetric encryption.
    """
    def __init__(self, key: str = "backup_secret"):
        """
        Initializes SecureBackup with an encryption key.

        Args:
            key: The secret key to encrypt and decrypt backups.
        """
        self.storage: Dict[str, str] = {}
        self.crypto = CryptoChat(key)

    def backup(self, key: str, data: str):
        """
        Encrypts and stores backup data.

        Args:
            key: The identification key for the backup.
            data: The data to be stored in the backup.
        """
        encrypted_data = self.crypto.encrypt(data)
        self.storage[key] = encrypted_data
        print(f"Secure backup performed for: {key}")

    def restore(self, key: str) -> str | None:
        """
        Restores and decrypts data from a backup.

        Args:
            key: The identification key of the backup to be restored.

        Returns:
            The original decrypted data, or None if the backup is not found.
        """
        encrypted_data = self.storage.get(key)
        if encrypted_data:
            return self.crypto.decrypt(encrypted_data)
        return None
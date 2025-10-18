import base64

class CryptoSystem:
    @staticmethod
    def encrypt(data: str) -> bytes:
        """Encrypts data using a simple Base64 encoding."""
        return base64.b64encode(data.encode('utf-8'))

    @staticmethod
    def decrypt(encrypted_data: bytes) -> str:
        """Decrypts data using Base64 decoding."""
        return base64.b64decode(encrypted_data).decode('utf-8')
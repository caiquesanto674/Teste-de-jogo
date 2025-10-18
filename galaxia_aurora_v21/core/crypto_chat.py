class CryptoChat:
    """Simulates end-to-end message encryption and exchange."""
    def __init__(self, key="secret"):
        self.key = key

    def encrypt(self, msg: str) -> str:
        return ''.join(chr((ord(c) + len(self.key)) % 256) for c in msg)

    def decrypt(self, enc_msg: str) -> str:
        return ''.join(chr((ord(c) - len(self.key)) % 256) for c in enc_msg)

    def send(self, sender: str, receiver: str, msg: str) -> str:
        encrypted_msg = self.encrypt(msg)
        print(f"> [{sender} -> {receiver}] (encrypted): {encrypted_msg}")
        return encrypted_msg

    def receive(self, encrypted_msg: str) -> str:
        decrypted_msg = self.decrypt(encrypted_msg)
        print(f"Received message: {decrypted_msg}")
        return decrypted_msg
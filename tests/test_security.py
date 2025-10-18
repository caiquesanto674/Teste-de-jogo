import unittest
from src.security import AuthManager, CryptoChat, SecureBackup

class TestSecurity(unittest.TestCase):

    def test_auth_manager(self):
        """Testa o registro e autenticação de usuários."""
        auth = AuthManager()
        mfa_code = auth.register("testuser", "password123")
        self.assertTrue(auth.authenticate("testuser", "password123", mfa_code))
        self.assertFalse(auth.authenticate("testuser", "wrongpassword", mfa_code))
        self.assertFalse(auth.authenticate("testuser", "password123", "wrongcode"))

    def test_crypto_chat(self):
        """Testa a criptografia e descriptografia de mensagens."""
        chat = CryptoChat(key="testkey")
        original_message = "Hello, World!"
        encrypted_message = chat.encrypt(original_message)
        decrypted_message = chat.decrypt(encrypted_message)
        self.assertNotEqual(original_message, encrypted_message)
        self.assertEqual(original_message, decrypted_message)

    def test_secure_backup(self):
        """Testa o backup e restauração de dados."""
        backup = SecureBackup(key="backupkey")
        original_data = "This is some secret data."
        backup.backup("test_backup", original_data)
        restored_data = backup.restore("test_backup")
        self.assertEqual(original_data, restored_data)
        self.assertIsNone(backup.restore("nonexistent_backup"))

if __name__ == '__main__':
    unittest.main()
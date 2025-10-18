import uuid
import hashlib
import random
from typing import Dict, Any

# =================== SEGURANÇA E AUTENTICAÇÃO ===================

class AuthManager:
    """
    Gerencia o registro e a autenticação de usuários usando uma senha com salt
    e um código de autenticação de múltiplos fatores (MFA).
    """
    def __init__(self):
        """Inicializa o gerenciador de autenticação."""
        self.users: Dict[str, Dict[str, str]] = {}

    def register(self, login: str, password: str) -> str:
        """
        Registra um novo usuário com um salt e hash de senha e gera um código MFA.

        Args:
            login: O nome de usuário para o registro.
            password: A senha para o novo usuário.

        Returns:
            O código MFA gerado para o usuário.
        """
        salt = uuid.uuid4().hex
        pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        mfa_code = str(random.randint(100000, 999999))
        self.users[login] = {"salt": salt, "hash": pwd_hash, "mfa_code": mfa_code}
        print(f"Usuário {login} registrado. O código MFA foi gerado.")
        return mfa_code

    def authenticate(self, login: str, password: str, code: str) -> bool:
        """
        Autentica um usuário verificando o hash da senha e o código MFA.

        Args:
            login: O nome de usuário a ser autenticado.
            password: A senha a ser verificada.
            code: O código MFA a ser verificado.

        Returns:
            True se a autenticação for bem-sucedida, False caso contrário.
        """
        user = self.users.get(login)
        if not user: return False
        hash_check = hashlib.sha256((password + user['salt']).encode()).hexdigest()
        return hash_check == user["hash"] and code == user["mfa_code"]

# =================== CRIPTOGRAFIA BÁSICA (MENSAGENS) ===================

class CryptoChat:
    """
    Simula um sistema de chat com criptografia de ponta a ponta usando uma
    chave simétrica simples.
    """
    def __init__(self, key: str):
        """
        Inicializa o CryptoChat com uma chave de criptografia.

        Args:
            key: A chave secreta a ser usada para criptografia e descriptografia.
        """
        if not key:
            raise ValueError("A chave de criptografia não pode ser vazia.")
        self.key = key

    def encrypt(self, msg: str) -> str:
        """
        Criptografa uma mensagem usando a chave da instância.

        Args:
            msg: A mensagem a ser criptografada.

        Returns:
            A mensagem criptografada.
        """
        return ''.join(chr((ord(c) + len(self.key)) % 256) for c in msg)

    def decrypt(self, enc: str) -> str:
        """
        Descriptografa uma mensagem usando a chave da instância.

        Args:
            enc: A mensagem criptografada.

        Returns:
            A mensagem original.
        """
        return ''.join(chr((ord(c) - len(self.key)) % 256) for c in enc)

    def enviar(self, user_from: str, user_to: str, msg: str) -> str:
        """
        Criptografa e envia uma mensagem para outro usuário.

        Args:
            user_from: O remetente da mensagem.
            user_to: O destinatário da mensagem.
            msg: A mensagem a ser enviada.

        Returns:
            A mensagem criptografada.
        """
        enc = self.encrypt(msg)
        print(f"> [{user_from} -> {user_to}] (cifrada): {enc}")
        return enc

    def receber(self, enc: str) -> str:
        """
        Recebe e descriptografa uma mensagem.

        Args:
            enc: A mensagem criptografada recebida.

        Returns:
            A mensagem original.
        """
        dec = self.decrypt(enc)
        print(f"Mensagem recebida: {dec}")
        return dec

# =================== BACKUP ELOG CRIPTOGRAFADO ===================

class SecureBackup:
    """
    Gerencia o backup e a restauração de dados usando criptografia simétrica.
    """
    def __init__(self, key: str = "backup_secret"):
        """
        Inicializa o SecureBackup com uma chave de criptografia.

        Args:
            key: A chave secreta para criptografar e descriptografar os backups.
        """
        self.storage: Dict[str, str] = {}
        self.crypto = CryptoChat(key)

    def backup(self, key: str, data: str):
        """
        Criptografa e armazena os dados de backup.

        Args:
            key: A chave de identificação para o backup.
            data: Os dados a serem armazenados no backup.
        """
        encrypted_data = self.crypto.encrypt(data)
        self.storage[key] = encrypted_data
        print(f"Backup seguro realizado para: {key}")

    def restore(self, key: str) -> str | None:
        """
        Restaura e descriptografa os dados de um backup.

        Args:
            key: A chave de identificação do backup a ser restaurado.

        Returns:
            Os dados originais descriptografados, ou None se o backup não for encontrado.
        """
        encrypted_data = self.storage.get(key)
        if encrypted_data:
            return self.crypto.decrypt(encrypted_data)
        return None
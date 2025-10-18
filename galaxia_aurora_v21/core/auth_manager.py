import uuid
import hashlib
import random
from typing import Dict, Optional
from .character_system import Character

class AuthManager:
    """Manages users and MFA authentication."""
    def __init__(self):
        self.users: Dict[str, Dict[str, str]] = {}
        self.admin_users = {"Caíque de Jesus Santos": "Monarca"}
        self.logged_in_user: Optional[Character] = None

    def register(self, login: str, password: str):
        salt = uuid.uuid4().hex
        pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        mfa_code = str(random.randint(100000, 999999))
        self.users[login] = {"salt": salt, "hash": pwd_hash, "mfa_code": mfa_code}
        print(f"User '{login}' registered. MFA Code: {mfa_code}")

    def authenticate(self, login: str, password: str, code: str) -> bool:
        user = self.users.get(login)
        if not user:
            return False
        hash_check = hashlib.sha256((password + user['salt']).encode()).hexdigest()
        return hash_check == user["hash"] and code == user["mfa_code"]

    def login(self, character: 'Character'):
        self.logged_in_user = character
        if self.is_admin(character):
            print(f"Admin user 'Monarca' ({character.name}) logged in.")

    def is_admin(self, character: 'Character') -> bool:
        return character.name in self.admin_users
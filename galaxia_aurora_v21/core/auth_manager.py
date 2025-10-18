from .character_system import Character

class AuthManager:
    def __init__(self):
        self.admin_users = {"Caíque de Jesus Santos": "Monarca"}
        self.logged_in_user: Character = None

    def login(self, character: Character):
        self.logged_in_user = character
        if self.is_admin(character):
            print(f"Admin user 'Monarca' ({character.name}) logged in.")

    def is_admin(self, character: Character) -> bool:
        return character.name in self.admin_users and self.admin_users[character.name] == "Monarca"

    def get_user_privileges(self):
        if self.logged_in_user and self.is_admin(self.logged_in_user):
            return {"can_spawn_resources": True, "has_god_mode": True}
        return {"can_spawn_resources": False, "has_god_mode": False}
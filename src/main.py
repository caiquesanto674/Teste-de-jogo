import time
from src.security import AuthManager, CryptoChat, SecureBackup
from src.economy import Economy
from src.simulation import AIModule, MilitaryBase, ChatLog

def main():
    """Main function to run the simulation."""
    # Initialization of modules
    auth = AuthManager()
    chat = CryptoChat(key="base_secret_key")
    backup = SecureBackup(key="backup_secret_key")
    econ = Economy()
    chat_log = ChatLog()
    ia_stack = [
        AIModule("Defense/Tactics"),
        AIModule("Intelligent Market"),
        AIModule("Antispam/Message Command")
    ]

    # Admin registration/authentication
    mfa_code = auth.register("admin", "strong@password")
    print(f"The MFA code for the admin is: {mfa_code} (simulating secure delivery)")
    print("Login attempt...")
    is_authenticated = auth.authenticate("admin", "strong@password", mfa_code)
    print(f"Login successful: {is_authenticated}")

    if not is_authenticated:
        print("Authentication failed. Ending simulation.")
        return

    # Start military base with three characters
    base = MilitaryBase("Aurora Nexus", auth, chat, econ, backup, ia_stack, chat_log)
    base.add_personagem("Caíque", "Supreme Commander")
    base.add_personagem("Sydra Ryl", "Defense Chief")
    base.add_personagem("Pyra", "AI Technician")

    # Simulate flows
    for cycle in range(3):
        print(f"\n--- CYCLE {cycle+1} ---")
        base.ciclo()
        time.sleep(0.3)

    # Example of encrypted message
    enc = chat.enviar("Caíque", "Pyra", "Review perimeter, reinforce intelligent AI defense.")
    chat.receber(enc)

    # Example of backup restoration
    backup_keys = list(backup.storage.keys())
    if backup_keys:
        latest_backup_key = backup_keys[-1]
        restored_data = backup.restore(latest_backup_key)
        print(f"\n--- Backup Restoration ---")
        print(f"Data restored from '{latest_backup_key}': {restored_data}")

if __name__ == "__main__":
    main()
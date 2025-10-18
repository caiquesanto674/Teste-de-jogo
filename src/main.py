import time
from src.security import AuthManager, CryptoChat, SecureBackup
from src.economy import Economy
from src.simulation import AIModule, MilitaryBase, ChatLog

def main():
    """Função principal para executar a simulação."""
    # Inicialização dos módulos
    auth = AuthManager()
    chat = CryptoChat(key="chave_secreta_da_base")
    backup = SecureBackup(key="chave_secreta_de_backup")
    econ = Economy()
    chat_log = ChatLog()
    ia_stack = [
        AIModule("Defesa/Tática"),
        AIModule("Mercado Inteligente"),
        AIModule("Antispam/Comando Mensagem")
    ]

    # Registro/autenticação do admin
    mfa_code = auth.register("admin", "senha@forte")
    print(f"O código MFA para o admin é: {mfa_code} (simulando entrega segura)")
    print("Tentativa de login...")
    is_authenticated = auth.authenticate("admin", "senha@forte", mfa_code)
    print(f"Login bem-sucedido: {is_authenticated}")

    if not is_authenticated:
        print("Falha na autenticação. Encerrando a simulação.")
        return

    # Inicia base militar com três personagens
    base = MilitaryBase("Aurora Nexus", auth, chat, econ, backup, ia_stack, chat_log)
    base.add_personagem("Caíque", "Comandante Supremo")
    base.add_personagem("Sydra Ryl", "Chefe Defesa")
    base.add_personagem("Pyra", "Técnica AI")

    # Simula fluxos
    for ciclo in range(3):
        print(f"\n--- CICLO {ciclo+1} ---")
        base.ciclo()
        time.sleep(0.3)

    # Exemplo de mensagem cifrada
    enc = chat.enviar("Caíque", "Pyra", "Revisar perímetro, reforçar defesa inteligente AI.")
    chat.receber(enc)

    # Exemplo de restauração de backup
    backup_keys = list(backup.storage.keys())
    if backup_keys:
        latest_backup_key = backup_keys[-1]
        restored_data = backup.restore(latest_backup_key)
        print(f"\n--- Restauração de Backup ---")
        print(f"Dados restaurados de '{latest_backup_key}': {restored_data}")

if __name__ == "__main__":
    main()
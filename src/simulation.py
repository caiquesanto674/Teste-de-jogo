import random
from datetime import datetime
from typing import List, Dict, Any
from src.security import AuthManager, CryptoChat, SecureBackup
from src.economy import Economy

# =================== AI/NARRATIVE/MULTILAYER PROTECTION ===================

class AIModule:
    """
    Represents an Artificial Intelligence module with analysis, logging,
    and self-learning capabilities.
    """
    def __init__(self, name: str):
        """
        Initializes the AI module.

        Args:
            name: The name of the AI module.
        """
        self.name = name
        self.version: float = 1.0
        self.log: List[str] = []

    def analyze(self, context: str) -> str:
        """
        Analyzes a given context and returns a status response.

        Args:
            context: The context to be analyzed.

        Returns:
            The status response of the analysis.
        """
        ts = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.log.append(f"{ts}: [{self.name}] analysis: {context}")
        if "attack" in context or "hack" in context:
            return "AI Defense activated."
        if "market" in context:
            return "AI market analysis done."
        if "message" in context:
            return "Anti-fake protection verified."
        return "Regular AI Status."

    def auto_learn(self):
        """
        Simulates the self-learning process, with a chance to increase the
        version of the AI module.
        """
        if random.random() > 0.58:
            self.version += 0.01
            print(f"AI '{self.name}' upgrade: version {self.version:.2f}")

# =================== CHARACTERS AND BEHAVIORAL PHRASES ===================

class Character:
    """
    Represents a character in the game, with a name, role, level, and a set
    of behavioral phrases.
    """
    def __init__(self, name: str, role: str):
        """
        Initializes a new character.

        Args:
            name: The name of the character.
            role: The function or role of the character.
        """
        self.name = name
        self.role = role
        self.level: int = 1
        self.confirm_code: str = f"CONFIRM_{role.upper()}_{random.randint(100, 999)}"
        self.phrases: List[str] = [
            f"{role} '{name}': Base under control. {self.confirm_code}",
            f"{role} '{name}': Sector secure, monitoring.",
            f"{role} '{name}': AI command received and encoded.",
            f"{role} '{name}': Level {self.level}, ready for action."
        ]
    def falar(self) -> str:
        """
        Returns a random phrase from the character's set of phrases.

        Returns:
            A random behavioral phrase.
        """
        return random.choice(self.phrases[1:])

# =================== CHAT LOG AND ATTITUDES ===================

class ChatLog:
    """
    Records and displays a log of messages and actions that occur in the simulation.
    """
    def __init__(self):
        """Initializes the chat log."""
        self.log: List[Dict[str, Any]] = []
    def enviar(self, user: str, msg: str):
        """
        Adds a new log entry.

        Args:
            user: The user who is performing the action.
            msg: The message or action to be recorded.
        """
        registro = {"user": user, "msg": msg, "hora": datetime.now().strftime("%d/%m/%Y %H:%M")}
        self.log.append(registro)
    def ver_log(self, ultimos: int = 5):
        """
        Displays the last entries of the log.

        Args:
            ultimos: The number of last entries to be displayed.
        """
        print("\n---- Last messages/actions ----")
        for item in self.log[-ultimos:]:
            print(f"[{item['hora']}] {item['user']}: {item['msg']}")

# =================== MILITARY BASE (CORE) ===================

class MilitaryBase:
    """
    The main class that represents the military base and orchestrates the simulation.
    """
    def __init__(self, name: str, auth: AuthManager, chat: CryptoChat, econ: Economy, backup: SecureBackup, ia_cams: List[AIModule], chat_log: ChatLog):
        """
        Initializes the military base with all its modules.

        Args:
            name: The name of the military base.
            auth: The authentication manager.
            chat: The encrypted chat system.
            econ: The economy system.
            backup: The secure backup system.
            ia_cams: A list of AI modules.
            chat_log: The chat log.
        """
        self.nome = name
        self.auth = auth
        self.chat = chat
        self.econ = econ
        self.backup = backup
        self.ia_cams = ia_cams
        self.chat_log = chat_log
        self.personagens: List[Character] = []
        self.defesa: int = 3

    def add_personagem(self, name: str, function: str):
        """
        Adds a new character to the military base.

        Args:
            name: The name of the new character.
            function: The function of the new character.
        """
        novo = Character(name, function)
        self.personagens.append(novo)
        frase = novo.falar()
        self.chat_log.enviar(novo.name, f"New character active: {frase}")

    def ciclo(self):
        """
        Executes a single simulation cycle, which includes updating the economy,
        AI analysis, character actions, and data backup.
        """
        print(f"\n==== Operations cycle: {datetime.now().strftime('%d/%m/%Y %H:%M')} ====")
        self.econ.update()
        respostas_ia = [ia.analyze("attack, market, message") for ia in self.ia_cams]
        self.defesa += random.choice([0, 1])  # Simulation of events
        for ia in self.ia_cams:
            ia.auto_learn()

        for p in self.personagens:
            frase = p.falar()
            print(frase)
            self.chat_log.enviar(p.name, frase)

        self.backup.backup(f"backup_{self.nome}_{datetime.now().strftime('%H%M%S')}", str({"econ": self.econ.balance, "defesa": self.defesa}))
        print(f"Current defense: {self.defesa} | Balance: {self.econ.balance:.2f} | Technology: {self.econ.tech:.2f}")
        self.chat_log.ver_log()
        print("----------- End of cycle -----------\n")
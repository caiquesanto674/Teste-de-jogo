import random
from datetime import datetime
from typing import List, Dict, Any
from src.security import AuthManager, CryptoChat, SecureBackup
from src.economy import Economy

# =================== IA/NARRATIVA/PROTEÇÃO MULTICAMADA ===================

class AIModule:
    """
    Representa um módulo de Inteligência Artificial com capacidade de análise,
    log e auto-aprendizagem.
    """
    def __init__(self, name: str):
        """
        Inicializa o módulo de IA.

        Args:
            name: O nome do módulo de IA.
        """
        self.name = name
        self.version: float = 1.0
        self.log: List[str] = []

    def analyze(self, contexto: str) -> str:
        """
        Analisa um determinado contexto e retorna uma resposta de status.

        Args:
            contexto: O contexto a ser analisado.

        Returns:
            A resposta de status da análise.
        """
        ts = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.log.append(f"{ts}: [{self.name}] análise: {contexto}")
        if "ataque" in contexto or "hack" in contexto:
            return "Defesa IA ativada."
        if "mercado" in contexto:
            return "Análise de mercado IA feita."
        if "mensagem" in contexto:
            return "Proteção anti-fake verificada."
        return "Status IA regular."

    def auto_learn(self):
        """
        Simula o processo de auto-aprendizagem, com uma chance de aumentar a
        versão do módulo de IA.
        """
        if random.random() > 0.58:
            self.version += 0.01
            print(f"AI '{self.name}' upgrade: versão {self.version:.2f}")

# =================== PERSONAGENS E FRASES DE COMPORTAMENTO ===================

class Character:
    """
    Representa um personagem no jogo, com um nome, função, nível e um conjunto
    de frases de comportamento.
    """
    def __init__(self, name: str, role: str):
        """
        Inicializa um novo personagem.

        Args:
            name: O nome do personagem.
            role: A função ou papel do personagem.
        """
        self.name = name
        self.role = role
        self.level: int = 1
        self.confirm_code: str = f"CONFIRM_{role.upper()}_{random.randint(100, 999)}"
        self.phrases: List[str] = [
            f"{role} '{name}': Base sob controle. {self.confirm_code}",
            f"{role} '{name}': Setor seguro, monitorando.",
            f"{role} '{name}': Comando IA recebido e codificado.",
            f"{role} '{name}': Nível {self.level}, pronto para ação."
        ]
    def falar(self) -> str:
        """
        Retorna uma frase aleatória do conjunto de frases do personagem.

        Returns:
            Uma frase de comportamento aleatória.
        """
        return random.choice(self.phrases)

# =================== LOG DE CHAT E ATITUDES ===================

class ChatLog:
    """
    Registra e exibe um log de mensagens e ações que ocorrem na simulação.
    """
    def __init__(self):
        """Inicializa o log de chat."""
        self.log: List[Dict[str, Any]] = []
    def enviar(self, user: str, msg: str):
        """
        Adiciona uma nova entrada de log.

        Args:
            user: O usuário que está realizando a ação.
            msg: A mensagem ou ação a ser registrada.
        """
        registro = {"user": user, "msg": msg, "hora": datetime.now().strftime("%d/%m/%Y %H:%M")}
        self.log.append(registro)
    def ver_log(self, ultimos: int = 5):
        """
        Exibe as últimas entradas do log.

        Args:
            ultimos: O número de últimas entradas a serem exibidas.
        """
        print("\n---- Últimas mensagens/ações ----")
        for item in self.log[-ultimos:]:
            print(f"[{item['hora']}] {item['user']}: {item['msg']}")

# =================== BASE MILITAR (NÚCLEO) ===================

class MilitaryBase:
    """
    A classe principal que representa a base militar e orquestra a simulação.
    """
    def __init__(self, nome: str, auth: AuthManager, chat: CryptoChat, econ: Economy, backup: SecureBackup, ia_cams: List[AIModule], chat_log: ChatLog):
        """
        Inicializa a base militar com todos os seus módulos.

        Args:
            nome: O nome da base militar.
            auth: O gerenciador de autenticação.
            chat: O sistema de chat criptografado.
            econ: O sistema de economia.
            backup: O sistema de backup seguro.
            ia_cams: Uma lista de módulos de IA.
            chat_log: O log de chat.
        """
        self.nome = nome
        self.auth = auth
        self.chat = chat
        self.econ = econ
        self.backup = backup
        self.ia_cams = ia_cams
        self.chat_log = chat_log
        self.personagens: List[Character] = []
        self.defesa: int = 3

    def add_personagem(self, nome: str, funcao: str):
        """
        Adiciona um novo personagem à base militar.

        Args:
            nome: O nome do novo personagem.
            funcao: A função do novo personagem.
        """
        novo = Character(nome, funcao)
        self.personagens.append(novo)
        frase = novo.falar()
        self.chat_log.enviar(novo.name, f"Novo personagem ativo: {frase}")

    def ciclo(self):
        """
        Executa um único ciclo de simulação, que inclui a atualização da economia,
        a análise da IA, as ações dos personagens e o backup dos dados.
        """
        print(f"\n==== Ciclo de operações: {datetime.now().strftime('%d/%m/%Y %H:%M')} ====")
        self.econ.update()
        respostas_ia = [ia.analyze("ataque, mercado, mensagem") for ia in self.ia_cams]
        self.defesa += random.choice([0, 1])  # Simulação de eventos
        for ia in self.ia_cams:
            ia.auto_learn()

        for p in self.personagens:
            frase = p.falar()
            print(frase)
            self.chat_log.enviar(p.name, frase)

        self.backup.backup(f"backup_{self.nome}_{datetime.now().strftime('%H%M%S')}", str({"econ": self.econ.balance, "defesa": self.defesa}))
        print(f"Defesa atual: {self.defesa} | Saldo: {self.econ.balance:.2f} | Tecnologia: {self.econ.tech:.2f}")
        self.chat_log.ver_log()
        print("----------- Fim do ciclo -----------\n")
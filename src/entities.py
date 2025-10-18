# ==================== MÓDULO 4: PERSONAGENS E PODER PSICOLÓGICO ====================
class Character:
    """
    Representa um personagem no jogo, com um nome e um nível de volição que
    influencia suas ações.
    """
    def __init__(self, name: str, volicao_level: int = 10):
        """
        Inicializa um novo personagem.

        Args:
            name: O nome do personagem.
            volicao_level: O nível de volição do personagem.
        """
        self.name = name
        self.volicao_level = volicao_level

    def confirm_action(self, action: str):
        """
        Imprime uma mensagem de confirmação de ação, que inclui o nome do
        personagem e seu nível de volição.

        Args:
            action: A ação a ser confirmada.
        """
        print(f"[CÓDIGO DE COMPORTAMENTO]: Agente {self.name} (Volição: {self.volicao_level}) confirma ação: '{action}'.")
from src.actions import ActionType

class AgentePPO:
    def __init__(self):
        """Inicializa o agente com um nível de agressividade."""
        self.agressividade = 0.5

    def decisao(self, ctx):
        """Toma uma decisão com base no contexto."""
        ctx['BT_ROOT'].executar(ctx['unidade'], ctx)
        if ctx['acao'] == ActionType.ATTACK_NORMAL and self.agressividade > 0.8:
            return ActionType.ATTACK_AGGRESSIVE
        return ctx['acao']
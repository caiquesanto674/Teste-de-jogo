class NoComportamento:
    def __init__(self, nome):
        """Inicializa um nó de comportamento."""
        self.nome = nome

    def executar(self, unidade, ctx):
        """Método a ser implementado nas subclasses."""
        raise NotImplementedError

class NoSelector(NoComportamento):
    def __init__(self, nome, *filhos):
        super().__init__(nome)
        self.filhos = filhos

    def executar(self, unidade, ctx):
        """Executa os filhos até que um tenha sucesso."""
        for filho in self.filhos:
            if filho.executar(unidade, ctx) == "SUCESSO":
                return "SUCESSO"
        return "FALHA"

class NoSequence(NoComportamento):
    def __init__(self, nome, *filhos):
        super().__init__(nome)
        self.filhos = filhos

    def executar(self, unidade, ctx):
        """Executa os filhos em sequência."""
        for filho in self.filhos:
            if filho.executar(unidade, ctx) == "FALHA":
                return "FALHA"
        return "SUCESSO"

from src.actions import ActionType

class AcaoAtacar(NoComportamento):
    def executar(self, unidade, ctx):
        """Verifica se a unidade pode atacar."""
        if unidade.ataque > 10:
            ctx['acao'] = ActionType.ATTACK_NORMAL
            return "SUCESSO"
        return "FALHA"

class AcaoRecuar(NoComportamento):
    def executar(self, unidade, ctx):
        """Verifica se a unidade deve recuar."""
        if unidade.hp < 20:
            ctx['acao'] = ActionType.FLEE
            return "SUCESSO"
        return "FALHA"

class AcaoBuscarSuporte(NoComportamento):
    def executar(self, unidade, ctx):
        """Verifica se a unidade deve buscar suporte."""
        if unidade.hp < 50 and ctx['suporte'] and ctx['suporte'].hp > 0:
            ctx['acao'] = ActionType.SEEK_SUPPORT
            return "SUCESSO"
        return "FALHA"

class AcaoAtacarEspecial(NoComportamento):
    def executar(self, unidade, ctx):
        """Verifica se a unidade pode usar o ataque especial."""
        if ctx['base'].recursos["Éter"] >= 1:
            ctx['acao'] = ActionType.ATTACK_SPECIAL
            return "SUCESSO"
        return "FALHA"
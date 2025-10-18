from src.utils import clamp
from src.behavior_tree import NoSelector, NoSequence, AcaoRecuar, AcaoBuscarSuporte, AcaoAtacar, AcaoAtacarEspecial
from src.actions import ActionType

class UnidadeMilitar:
    def __init__(self, nome, ataque, hp, agente_ia):
        """Inicializa uma unidade militar."""
        self.nome = nome
        self.hp = self.max_hp = hp
        self.ataque = ataque
        self.ia = agente_ia
        self.inimigos_prox = 0
        self.suporte = None

    def take_damage(self, damage):
        self.hp = clamp(self.hp - damage, 0, self.max_hp)

    def acao(self, alvo, suporte, base):
        """Executa uma ação com base na decisão da IA."""
        ctx = {
            'unidade': self,
            'alvo': alvo,
            'suporte': suporte,
            'base': base,
            'acao': ActionType.IDLE,
            'BT_ROOT': self.bt()
        }
        acao = self.ia.decisao(ctx)

        if acao == ActionType.ATTACK_SPECIAL:
            base.recursos["Éter"] -= 1
            alvo.take_damage(self.ataque * 3)
            return f"{self.nome} usa um ataque especial devastador em {alvo.nome}!"
        elif acao == ActionType.ATTACK_AGGRESSIVE:
            alvo.take_damage(self.ataque * 1.5)
            return f"{self.nome} usa um ataque agressivo em {alvo.nome}!"
        elif acao == ActionType.ATTACK_NORMAL:
            alvo.take_damage(self.ataque)
            return f"{self.nome} ataca {alvo.nome}."
        elif acao == ActionType.FLEE:
            return f"{self.nome} recua da batalha."
        elif acao == ActionType.SEEK_SUPPORT:
            self.hp = clamp(self.hp + 30, 0, self.max_hp)
            return f"{self.nome} busca suporte e se cura."
        return f"{self.nome} está ocioso."

    def bt(self):
        """Define a árvore de comportamento da unidade."""
        return NoSelector("Main",
            NoSequence("Ataque Especial", AcaoAtacarEspecial("Atacar Especial")),
            NoSequence("Sobrevivência", AcaoRecuar("Recuar")),
            NoSequence("Suporte", AcaoBuscarSuporte("Buscar Suporte")),
            AcaoAtacar("Atacar")
        )

class UnidadeSuporte(UnidadeMilitar):
    def acao(self, alvo, sup):
        """Cura uma unidade aliada."""
        if alvo.hp <= 70:
            alvo.hp = clamp(alvo.hp + 20, 0, alvo.max_hp)
            return f"{self.nome} cura {alvo.nome}."
        return f"{self.nome} não vê necessidade de curar."
from abc import ABC, abstractmethod

class UnidadeMilitar(ABC):
    def __init__(self, nome, patente):
        self.nome = nome
        self.patente = patente

    @abstractmethod
    def agir(self):
        pass

    def frase_batalha(self, evento):
        frases = {
            "ataque": "Avançar, manter formação!",
            "defesa": "Segurem a linha! Não recuem!",
            "confirmação": "Ordem recebida, senhor!",
        }
        return frases.get(evento, "Aguardando ordens.")

class Soldado(UnidadeMilitar):
    def agir(self):
        return "Marchando na direção dos recursos."

class Oficial(UnidadeMilitar):
    def agir(self):
        return "Planejando estratégia para captura de base inimiga."

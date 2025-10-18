from src.utils import clamp

class Economia:
    def __init__(self):
        """Inicializa a produção de recursos."""
        self.producao = {"Energia": 10, "Metal": 5, "Comida Rara": 1, "Éter": 0.1}

    def gerar(self, base):
        """Gera recursos com base na moral da base."""
        fator = max(0.25, base.moral / 100)
        for recurso, valor in self.producao.items():
            base.recursos[recurso] += int(valor * fator)
        return "Produção realizada."

class BaseMilitar:
    def __init__(self, nome="Solaris"):
        """Inicializa a base militar com nome e recursos."""
        self.nome = nome
        self.nivel = 1
        self.recursos = {"Energia": 100, "Metal": 20, "Comida Rara": 2, "Éter": 1}
        self.moral = 80
        self.moral_max = 100

    def aplicar_impacto(self, impacto):
        """Aplica um impacto à moral da base."""
        self.moral = clamp(self.moral + impacto, 0, self.moral_max)
        return f"Moral atual: {self.moral}"
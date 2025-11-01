class Economia:
    def __init__(self, initial_resources):
        self.recursos = initial_resources

    def produzir(self, recurso, quantidade):
        self.recursos[recurso] += quantidade
        return f"{quantidade} unidades de {recurso} produzidas."

    def consumir(self, recurso, quantidade):
        if self.recursos[recurso] >= quantidade:
            self.recursos[recurso] -= quantidade
            return f"{quantidade} unidades de {recurso} consumidas."
        else:
            return f"Recursos insuficientes de {recurso}."

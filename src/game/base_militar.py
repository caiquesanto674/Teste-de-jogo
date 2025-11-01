import json
import os
from .unidade_militar import UnidadeMilitar
from .economia import Economia

class BaseMilitar:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'config.json')
        with open(config_path) as f:
            config = json.load(f)
        self.nome = config['base_name']
        self.unidades = []
        self.economia = Economia(config['initial_resources'])
        self.evento_log = []

    def adicionar_unidade(self, unidade: UnidadeMilitar):
        self.unidades.append(unidade)
        self.evento_log.append(f"{unidade.nome} ({unidade.patente}) foi integrado à base.")

    def status_base(self):
        return f"Unidades: {len(self.unidades)}, Recursos: {self.economia.recursos}"

    def registrar_evento(self, evento):
        self.evento_log.append(evento)
        return evento

    def find_and_fix_bug(self):
        # Simulação de possível bug: recurso negativo
        for rec, qtd in self.economia.recursos.items():
            if qtd < 0:
                self.economia.recursos[rec] = 0
                self.registrar_evento(f"Bug corrigido: recurso {rec} negativo, redefinido para 0.")
        return "Varredura de bugs concluída."

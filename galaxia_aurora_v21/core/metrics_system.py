import random

class MetricXValidator:
    """
    [PT] Analisa desempenho, impacto e velocidade (latência, felicidade).
    [EN] Analyzes performance, impact and speed (latency, morale).
    """

    def validate(self, effectiveness: float):
        impact = effectiveness * random.uniform(0.8, 1.0)
        latency_ms = random.uniform(50, 100) * 0.7
        morale = random.choice([True, False])
        return impact, latency_ms, morale
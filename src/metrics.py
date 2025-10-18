import random

# ==================== MÓDULO 6: MÉTRICA X AVANÇADA (Pato X Felicidade) ====================
class MetricXValidator:
    """
    Valida e calcula métricas de desempenho avançadas, como impacto estratégico
    (Felicidade) e latência de comando (Pato).
    """
    def validate(self, volicao_audacia: float):
        """
        Calcula as métricas de desempenho com base na audácia/volição do jogador.

        Args:
            volicao_audacia: O nível atual de audácia/volição.

        Returns:
            Uma tupla contendo o impacto da felicidade, a latência do pato e o status
            de compartilhamento de dados.
        """
        # Impacto (Felicidade): Escala pela Audácia (Volição), recompensando decisões agressivas
        impact_felicidade = volicao_audacia * random.uniform(0.9, 1.1)
        # Latência (Pato): Simulação de tempo, otimizado pelo Tech Level (Universidade Total)
        latency_pato_ms = random.uniform(40, 80) * 0.65
        # Animac 20: Compartilhamento de dados/status
        data_share = True
        return impact_felicidade, latency_pato_ms, data_share
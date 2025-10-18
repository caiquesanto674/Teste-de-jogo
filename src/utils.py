import random

def clamp(value, min_value, max_value):
    """Restringe um valor entre um mínimo e um máximo."""
    return max(min_value, min(value, max_value))

def frase(tipo):
    """Retorna uma frase aleatória com base no tipo fornecido."""
    frases = {
        "romance": ["Vínculo fortalecido!", "Elo emocional ativo.", "Relação melhorada."],
        "gestao": ["Gestão reforçada!", "Base estável.", "Administração eficaz."],
        "tecnologia": ["Tecnologia aprimorada!", "Pesquisa concluída.", "Upgrade realizado."]
    }
    return random.choice(frases.get(tipo, ["Comando ok."]))
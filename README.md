# Simulação de Comando e Segurança

Este projeto é uma simulação de um centro de comando militar, escrito em Python, com foco em segurança, economia e operações de IA.

## Visão Geral

O projeto é estruturado da seguinte forma:

- `src/`: Contém todo o código-fonte da simulação.
  - `main.py`: O ponto de entrada principal para executar a simulação.
  - `security.py`: Contém as classes para autenticação, criptografia e backup.
  - `economy.py`: Gerencia a economia da base e o mercado.
  - `simulation.py`: Contém as classes para a simulação principal, incluindo a base militar, personagens e IA.
- `tests/`: Contém os testes de unidade para o projeto.

## Como Executar a Simulação

Para executar a simulação, execute o seguinte comando na raiz do projeto:

```bash
python3 -m src.main
```

## Como Executar os Testes

Para executar os testes de unidade, execute o seguinte comando na raiz do projeto:

```bash
python3 -m unittest discover tests
```
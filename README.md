# Simulação de Protocolo Avançado

Este projeto é uma simulação de um centro de comando avançado, escrito em Python, com foco em protocolos de poder, economia dinâmica, IA evolutiva e métricas de desempenho.

## Visão Geral

O projeto é estruturado da seguinte forma:

- `src/`: Contém todo o código-fonte da simulação.
  - `main.py`: O ponto de entrada principal para executar a simulação.
  - `services.py`: Contém o serviço de armazenamento em nuvem.
  - `economy.py`: Gerencia a economia do jogo.
  - `protocols.py`: Define os protocolos de poder e IA.
  - `entities.py`: Define as entidades do jogo, como personagens.
  - `metrics.py`: Contém o validador de métricas de desempenho.
  - `simulation.py`: Contém a classe principal da base militar que orquestra a simulação.
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
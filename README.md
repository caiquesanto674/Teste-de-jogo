# A Crônica do Comandante Solaris

Este projeto é uma simulação de um jogo de estratégia baseado em texto, escrito em Python. Ele apresenta um sistema de combate tático, gerenciamento de recursos e uma árvore de comportamento para a tomada de decisões da IA.

## Visão Geral

O projeto é estruturado da seguinte forma:

- `src/`: Contém todo o código-fonte da simulação.
  - `main.py`: O ponto de entrada principal para executar a simulação.
  - `actions.py`: Define as ações que as unidades podem realizar.
  - `agent.py`: Contém o agente de IA que toma decisões para as unidades.
  - `behavior_tree.py`: Implementa a lógica da árvore de comportamento.
  - `economy.py`: Gerencia a economia da base e a geração de recursos.
  - `units.py`: Define as unidades militares e suas habilidades.
  - `utils.py`: Funções utilitárias.
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
# Simulação de Estratégia Apolo

Este projeto é uma simulação de um jogo de estratégia em tempo real, escrito em Python, com foco em gerenciamento de recursos, desenvolvimento de tecnologia e automação de IA.

## Visão Geral

O projeto é estruturado da seguinte forma:

- `src/`: Contém todo o código-fonte da simulação.
  - `main.py`: O ponto de entrada principal para executar a simulação.
  - `core.py`: Contém a classe principal da base militar.
  - `economy.py`: Gerencia a economia do jogo, incluindo tecnologia e recursos.
  - `entities.py`: Define as entidades do jogo, como personagens.
  - `ai.py`: Contém o protocolo de IA para tomada de decisões autônomas.
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

## Como Executar com Docker

Para construir a imagem Docker e executar a simulação em um contêiner, use os seguintes comandos:

```bash
# Construir a imagem
docker build -t apolo-strategy .

# Executar a simulação
docker run apolo-strategy
```
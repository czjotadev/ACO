# 🐜 Ant System: Otimização de Rotas

Este projeto é uma implementação básica do algoritmo de Colônia de Formigas (Ant System - ACO) em Python. O objetivo é encontrar o caminho mais curto entre várias cidades, considerando distâncias simuladas, utilizando técnicas bioinspiradas.

---

## 📚 Descrição

O ACO é um algoritmo inspirado no comportamento das formigas reais, que utilizam trilhas de feromônio para encontrar os caminhos mais curtos para fontes de alimento. Essa abordagem é aplicada em problemas de otimização combinatória, como o problema do caixeiro viajante (TSP).

No algoritmo:
- **Feromônio** guia a exploração.
- **Visibilidade** (1/distância) favorece caminhos curtos.
- **Evaporação de feromônio** evita estagnação em soluções subótimas.

---

## 🚀 Como Funciona

1. **Distância**: Uma matriz de distâncias é calculada entre todas as cidades.
2. **Probabilidade**: Cada formiga escolhe o próximo destino com base no feromônio e na visibilidade.
3. **Atualização**: As trilhas de feromônio são atualizadas com base nas soluções construídas pelas formigas.
4. **Melhor Solução**: Após várias iterações, o caminho mais curto é identificado.

---

## 📂 Estrutura do Código

- **Parâmetros**: Definição de constantes como `alpha`, `beta`, `rho`, número de formigas e iterações.
- **Funções principais**:
  - `calculate_distance`: Calcula a distância euclidiana entre cidades.
  - `generate_distance_matrix`: Gera a matriz de distâncias.
  - `ant_system`: Implementa o algoritmo ACO.
- **Exemplo de uso**: Uma lista de cidades com coordenadas 2D é fornecida como entrada.

---

## 🧑‍💻 Como Executar

1. **Pré-requisitos**:
   - Python 3.x
   - Bibliotecas: `numpy`

2. **Instalação de dependências**:
   ```bash
   pip install numpy

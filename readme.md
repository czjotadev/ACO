# 🐜 Algoritmo de Colônia de Formigas (ACO) - Otimização de Rotas

Este repositório implementa o algoritmo de **Colônia de Formigas (ACO)** para resolver problemas de otimização de rotas, como o problema do caixeiro viajante (TSP). O algoritmo simula o comportamento de formigas em busca do melhor caminho entre várias cidades, com base na quantidade de feromônio nas arestas.

---

## 📑 Descrição do Algoritmo

O algoritmo de **Colônia de Formigas (ACO)** é uma técnica de otimização inspirada no comportamento das formigas na natureza, que procuram o melhor caminho para fontes de alimento. As formigas deixam um rastro de **feromônio** à medida que se movem, e esse feromônio influencia as formigas subsequentes a seguir os caminhos mais promissores. Esse comportamento é utilizado para resolver problemas de otimização, como o **Problema do Caixeiro Viajante (TSP)**.

### Como o Algoritmo Funciona:

1. **Inicialização**:
   - O algoritmo começa com uma matriz de **feromônios** que é inicialmente distribuída de forma uniforme, representando a probabilidade de escolha de cada aresta.
   - A **matriz de distâncias** entre as cidades também é fornecida, representando o custo de transitar de uma cidade para outra.

2. **Construção de Caminhos**:
   - Durante cada iteração, as formigas começam no ponto inicial (cidade 0) e escolhem o próximo movimento baseado em dois fatores:
     - O **feromônio** nas arestas, que influencia a probabilidade de escolha.
     - A **distância** entre as cidades, que é invertida (cidades mais próximas têm mais chance de serem escolhidas).
   - A decisão de qual aresta tomar é ponderada pelos parâmetros `alfa` e `beta`, que controlam a influência do feromônio e da distância, respectivamente.

3. **Atualização de Feromônio**:
   - Após as formigas completarem suas rotas, o **feromônio** é atualizado:
     - As arestas dos **melhores caminhos** têm o feromônio aumentado, incentivando as formigas a seguir essas rotas.
     - A quantidade de feromônio nas arestas diminui ao longo do tempo, simulando a evaporação natural do feromônio.

4. **Evaporação**:
   - O **feromônio** evapora a cada iteração, o que significa que rotas que não são escolhidas por várias iterações perdem seu atrativo, enquanto as rotas mais visitadas pelas formigas aumentam suas chances de serem escolhidas no futuro.

5. **Iterações**:
   - O algoritmo executa um número definido de iterações, onde as formigas exploram o espaço de soluções e o feromônio é atualizado.
   - Ao final do processo, o algoritmo retorna o **melhor caminho** encontrado, que representa a solução para o problema de otimização.

### Parâmetros do Algoritmo:
- **distancias**: Matriz de distâncias entre as cidades.
- **n_formigas**: Número de formigas que irão explorar o problema.
- **n_melhores**: Número de melhores caminhos a serem usados para a atualização do feromônio.
- **n_iteracoes**: Número de iterações do algoritmo.
- **decaimento**: Taxa de evaporação do feromônio.
- **alfa (α)**: Importância do feromônio na escolha do movimento das formigas.
- **beta (β)**: Importância da visibilidade (distância) na escolha do movimento.

---

## 🧑‍💻 Como Executar

1. **Pré-requisitos**:
   - Python 3.x
   - Bibliotecas: `numpy`

2. **Instalação de dependências**:
   ```bash
   pip install numpy

3. **Executando o código**:
   ```bash
   python index.py
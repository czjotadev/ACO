import numpy as np
import random

# Parâmetros do algoritmo
alpha = 1.0  # Importância do feromônio
beta = 2.0   # Importância da visibilidade
rho = 0.5    # Taxa de evaporação do feromônio
Q = 100      # Quantidade de feromônio depositada
num_ants = 10  # Número de formigas
num_iterations = 100  # Número de iterações

# Função de distância entre cidades (pode ser substituído por distâncias reais)
def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Gerar distâncias para as cidades
def generate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return distance_matrix

# Função para o algoritmo Ant System
def ant_system(cities):
    num_cities = len(cities)
    distance_matrix = generate_distance_matrix(cities)
    
    # Inicializar feromônio e visibilidade
    pheromone = np.ones((num_cities, num_cities))  # Inicialmente, todas as arestas têm feromônio 1
    visibility = 1 / (distance_matrix + np.eye(num_cities))  # Visibilidade é 1/distância (evitar div por 0)

    best_path = None
    best_path_length = float('inf')

    for _ in range(num_iterations):
        all_paths = []
        all_path_lengths = []
        
        # Cada formiga constrói uma solução
        for _ in range(num_ants):
            path = [random.randint(0, num_cities - 1)]  # Iniciar em uma cidade aleatória
            while len(path) < num_cities:
                current_city = path[-1]
                probabilities = []
                
                # Calcular probabilidades para escolher a próxima cidade
                for next_city in range(num_cities):
                    if next_city not in path:
                        prob = (pheromone[current_city][next_city] ** alpha) * \
                               (visibility[current_city][next_city] ** beta)
                        probabilities.append(prob)
                    else:
                        probabilities.append(0)
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(range(num_cities), p=probabilities)
                path.append(next_city)
            
            # Completar o ciclo (voltar à cidade inicial)
            path.append(path[0])
            all_paths.append(path)
            
            # Calcular o comprimento do caminho
            path_length = sum(distance_matrix[path[i]][path[i + 1]] for i in range(num_cities))
            all_path_lengths.append(path_length)
        
        # Atualizar a melhor solução
        min_length = min(all_path_lengths)
        if min_length < best_path_length:
            best_path_length = min_length
            best_path = all_paths[all_path_lengths.index(min_length)]

        # Evaporação de feromônio
        pheromone *= (1 - rho)
        
        # Atualização do feromônio
        for i, path in enumerate(all_paths):
            for j in range(num_cities):
                city1, city2 = path[j], path[j + 1]
                pheromone[city1][city2] += Q / all_path_lengths[i]
                pheromone[city2][city1] += Q / all_path_lengths[i]  # Grafo não direcionado

    return best_path, best_path_length

# Exemplo de cidades (coordenadas 2D)
cities = [(0, 0), (1, 5), (5, 1), (8, 6), (3, 7)]
best_path, best_path_length = ant_system(cities)

print("Melhor caminho:", best_path)
print("Comprimento do melhor caminho:", best_path_length)

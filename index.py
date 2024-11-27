from ant_system import ColoniaDeFormigas
import numpy as np

distancias = np.array([
    [0, 5.09901951, 5.38516481, 10.63014581, 7.81024968, 2.82842712],
    [5.09901951, 0, 6.40312424, 9.21954446, 5.38516481, 3.60555128],
    [5.38516481, 6.40312424, 0, 7.61577965, 6.40312424, 3.60555128],
    [10.63014581, 9.21954446, 7.61577965, 0, 5.83095189, 6.40312424],
    [7.81024968, 5.38516481, 6.40312424, 5.83095189, 0, 5.83095189],
    [2.82842712, 3.60555128, 3.60555128, 6.40312424, 5.83095189, 0],
])

colonia = ColoniaDeFormigas(distancias, len(distancias), 1, len(distancias) * 10, 0.5, alfa=1, beta=1)
caminho_mais_curto = colonia.executar()

caminho, distancia = caminho_mais_curto
caminho_real = [[int(a), int(b)] for a, b in caminho]

print(f"Caminho mais curto: {caminho_real}, Distância: {distancia}")
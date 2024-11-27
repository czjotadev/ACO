import numpy as np

class ColoniaDeFormigas:
    def __init__(self, distancias, n_formigas, n_melhores, n_iteracoes, decaimento, alfa=1, beta=1):
        self.distancias = distancias
        self.feromonio = np.ones(self.distancias.shape) / len(distancias)
        self.todos_indices = list(range(len(distancias)))
        self.n_formigas = n_formigas
        self.n_melhores = n_melhores
        self.n_iteracoes = n_iteracoes
        self.decaimento = decaimento
        self.alfa = alfa
        self.beta = beta

    def executar(self):
        caminho_mais_curto_todos_os_tempos = (None, np.inf)
        for i in range(self.n_iteracoes):
            print(f"\nIteração {i + 1}:")
            todos_caminhos = self.gerar_todos_caminhos()
            self.espalhar_feromonio(todos_caminhos)
            caminho_mais_curto = min(todos_caminhos, key=lambda x: x[1])
            if caminho_mais_curto[1] < caminho_mais_curto_todos_os_tempos[1]:
                caminho_mais_curto_todos_os_tempos = caminho_mais_curto
            self.feromonio *= self.decaimento
        return caminho_mais_curto_todos_os_tempos

    def espalhar_feromonio(self, todos_caminhos):
        caminhos_ordenados = sorted(todos_caminhos, key=lambda x: x[1])
        for caminho, _ in caminhos_ordenados[:self.n_melhores]:
            for u, v in caminho:
                self.feromonio[u, v] += 1.0 / self.distancias[u, v]

    def gerar_distancia_caminho(self, caminho):
        distancia_total = 0
        for u, v in caminho:
            distancia_total += self.distancias[u, v]
        return int(distancia_total)

    def gerar_todos_caminhos(self):
        todos_caminhos = []
        for i in range(self.n_formigas):
            caminho = self.gerar_caminho(0)
            distancia = self.gerar_distancia_caminho(caminho)
            todos_caminhos.append((caminho, distancia))
            caminho_convertido = [(int(u), int(v)) for u, v in caminho]
            print(f"Formiga {i + 1} - Caminho gerado: {caminho_convertido}, Distância: {distancia}")
        return todos_caminhos

    def gerar_caminho(self, inicio):
        caminho = []
        visitados = set()
        visitados.add(inicio)
        anterior = inicio
        for _ in range(len(self.distancias) - 1):
            movimento = self.escolher_movimento(self.feromonio[anterior], self.distancias[anterior], visitados)
            caminho.append((anterior, movimento))
            anterior = movimento
            visitados.add(movimento)
        caminho.append((anterior, inicio))
        return caminho

    def escolher_movimento(self, feromonio, dist, visitados):
        feromonio = np.copy(feromonio)
        feromonio[list(visitados)] = 0
        dist = np.where(dist == 0, 1e-10, dist)
        linha = feromonio ** self.alfa * ((1.0 / dist) ** self.beta)
        if linha.sum() == 0:
            linha_normalizada = np.ones_like(linha) / len(linha)
        else:
            linha_normalizada = linha / linha.sum()
        movimento = np.random.choice(self.todos_indices, 1, p=linha_normalizada)[0]
        return movimento
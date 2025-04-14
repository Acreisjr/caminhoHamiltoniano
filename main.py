def pode_visitar(candidato, etapa, caminho, matriz_adj):
    if matriz_adj[caminho[etapa - 1]][candidato] == 0:
        return False
    if candidato in caminho:
        return False
    return True

def busca_caminho(matriz_adj, caminho, etapa):
    if etapa == len(matriz_adj):
        return True
    for candidato in range(1, len(matriz_adj)):
        if pode_visitar(candidato, etapa, caminho, matriz_adj):
            caminho[etapa] = candidato
            if busca_caminho(matriz_adj, caminho, etapa + 1):
                return True
            caminho[etapa] = -1
    return False

def encontrar_caminho_hamiltoniano(matriz_adj):
    n = len(matriz_adj)
    caminho = [-1] * n
    caminho[0] = 0
    if not busca_caminho(matriz_adj, caminho, 1):
        return None
    return caminho

if __name__ == "__main__":
    grafo = [
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ]
    solucao = encontrar_caminho_hamiltoniano(grafo)
    if solucao:
        print("Caminho Hamiltoniano encontrado:")
        print(solucao)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")

import copy

grafo1 = {1:[2,3,6,7], 2:[1,3], 3:[1,2,4], 4:[3,5], 5:[4,6], 6:[1,5,7], 7:[1,6]}
grafo2 = {1:[2,3,6,7], 2:[1,3,6], 3:[1,2,4], 4:[3,5], 5:[4,6], 6:[1,2,5,7], 7:[1,6]}
grafo3 = {1:[2,3,6,7], 2:[1,3,5], 3:[1,2,4,7], 4:[3,5], 5:[2,4,6,7], 6:[1,5,7], 7:[1,3,5,6]}
grafo4 = {1:[2,3,6,7], 2:[1,3,5], 3:[1,2,4,7], 4:[3,5,6], 5:[2,4,6,7], 6:[1,4,5,7], 7:[1,3,5,6]}


grafos = {"Grafo 1": grafo1, "Grafo 2": grafo2, "Grafo 3": grafo3, "Grafo 4": grafo4}

def grau(grafo, vertice):
    return len(grafo[vertice])

def dirac(grafo):
    num_vertices = len(grafo)

    for vertice in grafo:
        if grau(grafo, vertice) < num_vertices / 2:
            return False

    return True

def ore(grafo):
    
    num_vertices = len(grafo)

    vertices = list(grafo.keys())

    for i, u in enumerate(vertices):
        for vertice in vertices[i+1:]:

            nao_adjacentes = vertice not in grafo[u]

            soma_insuficiente = grau(grafo, u) + grau(grafo, vertice) < num_vertices

            if nao_adjacentes and soma_insuficiente:
                return False

    return True

def bondy_chvatal(grafo):
    fechamento = copy.deepcopy(grafo)
    num_vertices = len(fechamento)
    houve_mudanca = True
    while houve_mudanca:

        houve_mudanca = False
        vertices = list(fechamento.keys())

        for i, u in enumerate(vertices):
            for vertice in vertices[i+1:]:

                nao_adjacentes = vertice not in fechamento[u]
                soma_graus_suficiente = grau(fechamento, u) + grau(fechamento, vertice) >= num_vertices
                
                if nao_adjacentes and soma_graus_suficiente:
                    fechamento[u].append(vertice)
                    fechamento[vertice].append(u)
                    houve_mudanca = True

    eh_completo = True
    
    for vertice in fechamento:
        if grau(fechamento, vertice) != num_vertices - 1:
            eh_completo = False

    return eh_completo


for nome, grafo in grafos.items():

    print(nome)
    print("Dirac:", "SIM" if dirac(grafo) else "NAO")
    print("Ore:", "SIM" if ore(grafo) else "NAO")
    print("Bondy-Chvatal:", "SIM" if bondy_chvatal(grafo) else "NAO")
    print()
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class GrafoD:
    def __init__(self):
        self.Ad = {}

    def add_edge(self, src, dest, weight):
        self.Ad.setdefault(src, []).append((dest, weight))

class Grafo:
    def __init__(self):
        self.Ad = {}

    def add_edge(self, src, dest, weight):
        self.Ad.setdefault(src, []).append((dest, weight))
        self.Ad.setdefault(dest, []).append((src, weight))


def bfs(graph, source):
    visited = set()
    queue = deque([(source, 0)])

    bfs_cost = {source: 0}  # Diccionario para almacenar los costos
    while queue:
        vertex, depth = queue.popleft()
        visited.add(vertex)

        #print("Visited:", vertex)
        #print("Depth:", depth)

        for neighbor, _ in graph.Ad[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
                visited.add(neighbor)
                bfs_cost[neighbor] = depth + 1

    return bfs_cost


# Funciones para ejecutar Dijkstra
def dijkstra(graph, source):
    distances = {source: 0}  # Diccionario para almacenar las distancias desde el origen
    pq = [(0, source)]  # Cola de prioridad para seleccionar el vértice con la menor distancia

    while pq:
        dist, vertex = heapq.heappop(pq)

        if dist > distances[vertex]:
            continue

        for neighbor, edge_weight in graph.Ad[vertex]:
            new_dist = dist + edge_weight

            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


def puertosIslas(Puertos, s, Islas, z, costoBarco, Puertosh, Islash):
    
    
    # Extraer cada costo C(s, pi) de s a pi luego de ejecutar Dijkstra(G, s, ω)
    puertos_cost = dijkstra(Puertos, s)

    # Inicializar el conjunto de costos de las islas
    islas_cost = {}

    # Ejecutar el algoritmo de Breadth-First Search en el grafo G' con cada isla qj
    for isla in Islash:
        islas_cost[isla] = bfs(Islas, isla)[z]

    min_cost = float('inf')
    besti = 0
    bestj = 0

 
    # Calcular el costo para cada combinación de puerto pi e isla qj y encontrar el mínimo
    for i in range(len(Puertosh)):
        for j in range(len(Islash)):
            costo = puertos_cost[Puertosh[i]] 
            print(puertos_cost[Puertosh[i]] )
            print(costo," 1")

            for x in costoBarco:
                if(x[0]== Puertosh[i] and x[1] == Islash[j] ):
                    costo = costo + x[2]
                    print(x[2])
                    print(costo," 2")
            costo = costo + islas_cost[Islash[j]]
            print(islas_cost[Islash[j]])
            print(costo, " 3")
            if costo < min_cost:
                min_cost = costo
                besti = i
                bestj = j

    return min_cost, besti, bestj


def main():
    Puertos = GrafoD()
    costosPuertos = [('S','A',2),('S','D',8),('A','S',3),('A','B',1),('A','D',3),('B','S',4),('B','C',6),('C','B',5),('C','D',9),('D','B',2),('D','C',2)]
    for puerto1, puerto2, costop in costosPuertos:
        Puertos.add_edge(puerto1, puerto2, costop)
    Islas = Grafo()
    costosIslas= [('1','4',2),('1','2',1),('2','4',3),('Z','2',12),('Z','5',2),('Z','3',5),('Z','6',2),('Z','8',3),('2','3',5),('4','5',1),('4','6',4),('6','7',3),('7','8',7),('3','7',4)]
    for islas1, islas2, costoi in costosIslas:
        Islas.add_edge(islas1, islas2, costoi)

    Puertosh= ['C','D']
    Islash= ['1','2','3']
    costoBarco = (['C','1',-12],['C','2',9],['C','3',7],['D','1',12],['D','2',-3],['D','3',21])

    min_cost, besti, bestj = puertosIslas(Puertos, 'S', Islas, 'Z', costoBarco, Puertosh, Islash)

    print("Minimum Cost:", min_cost)
    print("Best i:", besti)
    print("Best j:", bestj)
    return 0


main()
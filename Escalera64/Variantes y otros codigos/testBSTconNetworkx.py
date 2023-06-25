import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Graph:
    def __init__(self):
        self.Ad = {}

    def add_edge(self, src, dest, weight):
        self.Ad.setdefault(src, []).append((dest, weight))
        self.Ad.setdefault(dest, []).append((src, weight))

def get_edge_weight(u, v):
    # Función de peso arbitraria
    if (u, v) in [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]:
        return 2
    else:
        return 1

def bfs(graph, source, weight_func):
    visited = set()
    queue = deque([(source, 0)])

    bfs_cost = {source: 0}  # Diccionario para almacenar los costos
    while queue:
        vertex, weight = queue.popleft()
        visited.add(vertex)

        print("Visited:", vertex)
        print("Weight:", weight)

        for neighbor, edge_weight in graph.Ad[vertex]:
            if neighbor not in visited:
                cumulative_weight = weight + weight_func(vertex, neighbor)
                queue.append((neighbor, cumulative_weight))
                visited.add(neighbor)
                bfs_cost[neighbor] = cumulative_weight

    return bfs_cost

def draw_graph(graph, bfs_cost):
    G = nx.Graph()

    for src in graph.Ad:
        G.add_node(src)
        for dest, weight in graph.Ad[src]:
            G.add_edge(src, dest, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800, font_weight="bold")

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    node_labels = {}
    for node in G.nodes:
        node_labels[node] = f"Weight: {bfs_cost[node]}"
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='red', verticalalignment='bottom')

    plt.show()

def main():
    # Crear grafo
    graph = Graph()

    # Agregar aristas con pesos
    graph.add_edge('A', 'B', weight=2)
    graph.add_edge('B', 'C', weight=2)
    graph.add_edge('C', 'D', weight=2)
    graph.add_edge('D', 'E', weight=2)
    graph.add_edge('A', 'C', weight=1)

    # Ejecutar BFS y obtener el diccionario de costos
    bfs_cost = bfs(graph, 'A', get_edge_weight)

    # Dibujar grafo con los costos
    draw_graph(graph, bfs_cost)

if __name__ == "__main__":
    main()

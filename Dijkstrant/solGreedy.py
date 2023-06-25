import networkx as nx
import matplotlib.pyplot as plt
import heapq

class DGraph:
    def __init__(self):
        self.Ad = {}

    def add_edge(self, src, dest, weight):
        self.Ad.setdefault(src, []).append((dest, weight))

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

def draw_graph(graph, distances):
    G = nx.DiGraph()

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
        node_labels[node] = f"Distance: {distances[node]}"
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_color='red', verticalalignment='bottom')

    plt.show()

def main():
    # Crear grafo dirigido
    directed_graph = DGraph()
    directed_edges = [('X', 'Y', 5), ('Y', 'Z', 2), ('Z', 'W', 3), ('W', 'V', 1), ('X', 'Z', 4)]
    for src, dest, weight in directed_edges:
        directed_graph.add_edge(src, dest, weight=weight)

    # Agregar el nodo 'V'
    directed_graph.add_edge('V', 'X', weight=2)

    # Ejecutar Dijkstra y obtener el diccionario de distancias
    distances = dijkstra(directed_graph, 'X')

    # Dibujar grafo dirigido con las distancias
    draw_graph(directed_graph, distances)

    # Agregar pesos de las aristas y los vértices al segundo plot
    pos = nx.spring_layout(directed_graph)
    edge_labels = nx.get_edge_attributes(directed_graph, 'weight')
    node_labels = {node: f"Distance: {distances[node]}" for node in directed_graph.Ad}

    nx.draw_networkx_edge_labels(directed_graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(directed_graph, pos, labels=node_labels, font_color='red', verticalalignment='bottom')

    plt.show()

if __name__ == "__main__":
    main()
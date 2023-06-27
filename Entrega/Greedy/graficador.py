import networkx as nx
import matplotlib.pyplot as plt

# Crear los grafos
grafo_impares = nx.DiGraph()
grafo_medio = nx.Graph()
grafo_pares = nx.Graph()

# Definir las transiciones
transiciones = [
('1402858893', '204462795', 16),
('175795175', '1402858893', 14),
('204462795', '175795175', 8),
('1577027698', '95469452', 11),
('2104259464', '95469452', 19),
('1062186532', '2104259464', 2),
('859958504', '1577027698', 14),
('175795175', '1577027698', 15),
('175795175', '1062186532', -7),
('175795175', '859958504', 8),
('1402858893', '1577027698', 2),
('1402858893', '1062186532', 6),
('1402858893', '859958504', -9),
]

# Construir los grafos
for transicion in transiciones:
    nodo_a, nodo_b, costo = transicion
    # Grafo de Impares
    if int(nodo_a) % 2 != 0 and int(nodo_b) % 2 != 0:
        grafo_impares.add_edge(nodo_a, nodo_b, weight=costo)
    # Grafo del Medio
    elif int(nodo_a) % 2 != 0 and int(nodo_b) % 2 == 0:
        grafo_medio.add_edge(nodo_a, nodo_b, weight=costo)
    elif int(nodo_a) % 2 == 0 and int(nodo_b) % 2 != 0:
        grafo_medio.add_edge(nodo_b, nodo_a, weight=costo)
    # Grafo de Pares
    elif int(nodo_a) % 2 == 0 and int(nodo_b) % 2 == 0:
        grafo_pares.add_edge(nodo_a, nodo_b, weight=costo)

for nodo_a, nodo_b, _ in transiciones:
    if grafo_impares.has_edge(nodo_b, nodo_a):
        print(f"Transición opuesta (IMPAR - IMPAR): {nodo_b} -> {nodo_a} (Costo: {grafo_impares[nodo_b][nodo_a]['weight']})")

# Algoritmo de posicionamiento Fruchterman-Reingold
pos_impares = nx.spring_layout(grafo_impares, seed=42, k=100)
pos_medio = nx.spring_layout(grafo_medio, seed=42, k=100)
pos_pares = nx.spring_layout(grafo_pares, seed=42, k=100)

# Pedir al usuario el nodo inicial y final
nodo_inicial = input("Ingrese el nodo inicial: ")
nodo_final = input("Ingrese el nodo final: ")

# Crear la figura y los subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Grafo de Impares
nx.draw_networkx(grafo_impares, pos=pos_impares, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, arrows=True, ax=ax1)
edge_labels = nx.get_edge_attributes(grafo_impares, 'weight')
nx.draw_networkx_edge_labels(grafo_impares, pos=pos_impares, edge_labels=edge_labels, font_size=8, ax=ax1,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_impares.nodes:
    nx.draw_networkx_nodes(grafo_impares, pos=pos_impares, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax1)
    nx.draw_networkx_labels(grafo_impares, pos=pos_impares, labels={nodo_inicial: ''}, font_color='w', ax=ax1)
if nodo_final in grafo_impares.nodes:
    nx.draw_networkx_nodes(grafo_impares, pos=pos_impares, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax1)
    nx.draw_networkx_labels(grafo_impares, pos=pos_impares, labels={nodo_final: ''}, font_color='w', ax=ax1)
ax1.set_title('Grafo de Impares')

# Grafo del Medio
edge_list_medio = [(u, v, d) for u, v, d in grafo_medio.edges(data=True) if (int(u) % 2 != 0 and int(v) % 2 == 0) or (int(u) % 2 == 0 and int(v) % 2 != 0)]
grafo_medio_impares_pares = nx.Graph()
grafo_medio_impares_pares.add_edges_from(edge_list_medio)

nx.draw_networkx(grafo_medio_impares_pares, pos=pos_medio, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, ax=ax2)
edge_labels_medio = nx.get_edge_attributes(grafo_medio_impares_pares, 'weight')
nx.draw_networkx_edge_labels(grafo_medio_impares_pares, pos=pos_medio, edge_labels=edge_labels_medio, font_size=8, ax=ax2,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_medio_impares_pares.nodes:
    nx.draw_networkx_nodes(grafo_medio_impares_pares, pos=pos_medio, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax2)
    nx.draw_networkx_labels(grafo_medio_impares_pares, pos=pos_medio, labels={nodo_inicial: ''}, font_color='w', ax=ax2)
if nodo_final in grafo_medio_impares_pares.nodes:
    nx.draw_networkx_nodes(grafo_medio_impares_pares, pos=pos_medio, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax2)
    nx.draw_networkx_labels(grafo_medio_impares_pares, pos=pos_medio, labels={nodo_final: ''}, font_color='w', ax=ax2)
ax2.set_title('Grafo del Medio (Impares a Pares)')

# Grafo de Pares
nx.draw_networkx(grafo_pares, pos=pos_pares, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, ax=ax3)
edge_labels = nx.get_edge_attributes(grafo_pares, 'weight')
nx.draw_networkx_edge_labels(grafo_pares, pos=pos_pares, edge_labels=edge_labels, font_size=8, ax=ax3,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_pares.nodes:
    nx.draw_networkx_nodes(grafo_pares, pos=pos_pares, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax3)
    nx.draw_networkx_labels(grafo_pares, pos=pos_pares, labels={nodo_inicial: ''}, font_color='w', ax=ax3)
if nodo_final in grafo_pares.nodes:
    nx.draw_networkx_nodes(grafo_pares, pos=pos_pares, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax3)
    nx.draw_networkx_labels(grafo_pares, pos=pos_pares, labels={nodo_final: ''}, font_color='w', ax=ax3)
ax3.set_title('Grafo de Pares')

plt.tight_layout()
plt.show()

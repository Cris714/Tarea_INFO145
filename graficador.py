import networkx as nx
import matplotlib.pyplot as plt

# Crear los grafos
grafo_impares = nx.DiGraph()
grafo_medio = nx.Graph()
grafo_pares = nx.Graph()

# Definir las transiciones
transiciones = [
('1402858893', '204462795', 18),
('175795175', '1402858893', 8),
('95469453', '204462795', 14),
('1577027699', '204462795', 17),
('2104259465', '1577027699', 5),
('1062186533', '95469453', 14),
('859958505', '2104259465', 10),
('222422131', '1062186533', 12),
('364902757', '95469453', 0),
('204462795', '95469453', 19),
('1062186533', '1577027699', 20),
('175795175', '204462795', 20),
('1062186533', '1402858893', 8),
('2048021570', '1599430836', 0),
('860058000', '1599430836', 14),
('1396031018', '1599430836', 15),
('804170876', '2048021570', 17),
('1786320646', '1396031018', 19),
('469956286', '860058000', 3),
('772639058', '1396031018', 5),
('1555982812', '860058000', 4),
('1927465778', '2048021570', 1),
('860058000', '1555982812', 6),
('1062186533', '1786320646', -18),
('1062186533', '1396031018', -1),
('1062186533', '772639058', 14),
('1062186533', '860058000', 8),
('1577027699', '1786320646', -11),
('1577027699', '1396031018', -28),
('1577027699', '772639058', -14),
('1577027699', '860058000', -15),
('859958505', '1786320646', -18),
('859958505', '1396031018', -6),
('859958505', '772639058', 0),
('859958505', '860058000', -20),
('222422131', '1786320646', -2),
('222422131', '1396031018', 11),
('222422131', '772639058', -1),
('222422131', '860058000', 24),
('2104259465', '1786320646', -30),
('2104259465', '1396031018', -13),
('2104259465', '772639058', -8),
('2104259465', '860058000', 4),
('364902757', '1786320646', -12),
('364902757', '1396031018', 30),
('364902757', '772639058', -4),
('364902757', '860058000', 3),
('1402858893', '1786320646', 25),
('1402858893', '1396031018', 23),
('1402858893', '772639058', 8),
('1402858893', '860058000', -24),
('95469453', '1786320646', 0),
('95469453', '1396031018', -11),
('95469453', '772639058', 30),
('95469453', '860058000', -19),
('175795175', '1786320646', -26),
('175795175', '1396031018', 7),
('175795175', '772639058', -16),
('175795175', '860058000', 18),
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

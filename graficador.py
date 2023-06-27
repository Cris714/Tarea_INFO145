import networkx as nx
import matplotlib.pyplot as plt

# Crear los grafos
grafo_letras = nx.DiGraph()
grafo_medio = nx.Graph()
grafo_numeros = nx.Graph()

# Definir las transiciones
transiciones = [
('A', 'C', 25),
('A', 'E', 10),
('A', 'G', 3),
('B', 'A', 25),
('B', 'C', 1),
('B', 'E', 25),
('C', 'B', 4),
('C', 'D', 10),
('C', 'F', 5),
('C', 'G', 6),
('D', 'A', 1),
('D', 'B', 27),
('D', 'C', 3),
('D', 'E', 21),
('D', 'F', 16),
('E', 'B', 26),
('E', 'C', 23),
('E', 'G', 7),
('F', 'A', 2),
('F', 'B', 1),
('F', 'D', 10),
('F', 'E', 15),
('G', 'B', 6),
('G', 'D', 3),
('G', 'E', 14),
('0', '1', 5),
('0', '2', 21),
('0', '3', 14),
('0', '4', 16),
('1', '2', 21),
('2', '3', 28),
('2', '4', 24),
('2', '6', 16),
('3', '5', 15),
('3', '6', 16),
('D', '3', 9),
('D', '6', 5),
('C', '3', 15),
('C', '6', 17)
]

# Construir los grafos
for transicion in transiciones:
    nodo_a, nodo_b, costo = transicion
    # Grafo de Letras
    if nodo_a.isalpha() and nodo_b.isalpha():
        grafo_letras.add_edge(nodo_a, nodo_b, weight=costo)
    # Grafo del Medio
    elif nodo_a.isalpha() and nodo_b.isdigit():
        grafo_medio.add_edge(nodo_a, nodo_b, weight=costo)
    elif nodo_a.isdigit() and nodo_b.isalpha():
        grafo_medio.add_edge(nodo_b, nodo_a, weight=costo)
    # Grafo de Números
    elif nodo_a.isdigit() and nodo_b.isdigit():
        grafo_numeros.add_edge(nodo_a, nodo_b, weight=costo)

for nodo_a, nodo_b, _ in transiciones:
    if grafo_letras.has_edge(nodo_b, nodo_a):
        print(f"Transición opuesta (LETRA - LETRA): {nodo_b} -> {nodo_a} (Costo: {grafo_letras[nodo_b][nodo_a]['weight']})")
    if grafo_medio.has_edge(nodo_b, nodo_a):
        print(f"Transición opuesta (LETRA - NUMERO): {nodo_b} -> {nodo_a} (Costo: {grafo_medio[nodo_b][nodo_a]['weight']})")
    if grafo_numeros.has_edge(nodo_b, nodo_a):
        print(f"Transición opuesta (NUMERO - NUMERO):{nodo_b} -> {nodo_a} (Costo: {grafo_numeros[nodo_b][nodo_a]['weight']})")

# Algoritmo de posicionamiento Fruchterman-Reingold
pos_letras = nx.spring_layout(grafo_letras, seed=42, k=100)
pos_medio = nx.spring_layout(grafo_medio, seed=42, k=100)
pos_numeros = nx.spring_layout(grafo_numeros, seed=42, k=100)

# Pedir al usuario el nodo inicial y final
nodo_inicial = input("Ingrese el nodo inicial: ")
nodo_final = input("Ingrese el nodo final: ")

# Crear la figura y los subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Grafo de Letras
nx.draw_networkx(grafo_letras, pos=pos_letras, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, arrows=True, ax=ax1)
edge_labels = nx.get_edge_attributes(grafo_letras, 'weight')
nx.draw_networkx_edge_labels(grafo_letras, pos=pos_letras, edge_labels=edge_labels, font_size=8, ax=ax1,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_letras.nodes:
    nx.draw_networkx_nodes(grafo_letras, pos=pos_letras, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax1)
    nx.draw_networkx_labels(grafo_letras, pos=pos_letras, labels={nodo_inicial: ''}, font_color='w', ax=ax1)
if nodo_final in grafo_letras.nodes:
    nx.draw_networkx_nodes(grafo_letras, pos=pos_letras, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax1)
    nx.draw_networkx_labels(grafo_letras, pos=pos_letras, labels={nodo_final: ''}, font_color='w', ax=ax1)
ax1.set_title('Grafo de Letras')

# Grafo del Medio
nx.draw_networkx(grafo_medio, pos=pos_medio, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, ax=ax2)
edge_labels = nx.get_edge_attributes(grafo_medio, 'weight')
nx.draw_networkx_edge_labels(grafo_medio, pos=pos_medio, edge_labels=edge_labels, font_size=8, ax=ax2,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_medio.nodes:
    nx.draw_networkx_nodes(grafo_medio, pos=pos_medio, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax2)
    nx.draw_networkx_labels(grafo_medio, pos=pos_medio, labels={nodo_inicial: ''}, font_color='w', ax=ax2)
if nodo_final in grafo_medio.nodes:
    nx.draw_networkx_nodes(grafo_medio, pos=pos_medio, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax2)
    nx.draw_networkx_labels(grafo_medio, pos=pos_medio, labels={nodo_final: ''}, font_color='w', ax=ax2)
ax2.set_title('Grafo del Medio')

# Grafo de Números
nx.draw_networkx(grafo_numeros, pos=pos_numeros, with_labels=True, node_size=500, node_color='lightblue',
                 font_size=10, ax=ax3)
edge_labels = nx.get_edge_attributes(grafo_numeros, 'weight')
nx.draw_networkx_edge_labels(grafo_numeros, pos=pos_numeros, edge_labels=edge_labels, font_size=8, ax=ax3,
                             bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='white'))
if nodo_inicial in grafo_numeros.nodes:
    nx.draw_networkx_nodes(grafo_numeros, pos=pos_numeros, nodelist=[nodo_inicial], node_color='green',
                           node_size=500, ax=ax3)
    nx.draw_networkx_labels(grafo_numeros, pos=pos_numeros, labels={nodo_inicial: ''}, font_color='w', ax=ax3)
if nodo_final in grafo_numeros.nodes:
    nx.draw_networkx_nodes(grafo_numeros, pos=pos_numeros, nodelist=[nodo_final], node_color='green',
                           node_size=500, ax=ax3)
    nx.draw_networkx_labels(grafo_numeros, pos=pos_numeros, labels={nodo_final: ''}, font_color='w', ax=ax3)
ax3.set_title('Grafo de Números')

plt.tight_layout()
plt.show()

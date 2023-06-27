import networkx as nx
import matplotlib.pyplot as plt

# Crear los grafos
grafo_letras = nx.DiGraph()
grafo_medio = nx.Graph()
grafo_numeros = nx.Graph()

# Definir las transiciones
transiciones = [
('846930887', '1804289383', 14),
('1681692777', '846930887', 9),
('1714636915', '1681692777', 5),
('1957747793', '1681692777', 13),
('424238335', '1681692777', 19),
('719885387', '424238335', 0),
('1649760493', '1714636915', 12),
('596516649', '424238335', 9),
('1189641421', '846930887', 7),
('846930887', '1804289383', 14),
('1681692777', '846930887', 9),
('1714636915', '1681692777', 5),
('1957747793', '1681692777', 13),
('424238335', '1681692777', 19),
('719885387', '424238335', 0),
('1649760493', '1714636915', 12),
('596516649', '424238335', 9),
('1189641421', '846930887', 7),
('846930887', '1804289383', 14),
('1681692777', '846930887', 9),
('1714636915', '1681692777', 5),
('1957747793', '1681692777', 13),
('424238335', '1681692777', 19),
('719885387', '424238335', 0),
('1649760493', '1714636915', 12),
('596516649', '424238335', 9),
('1189641421', '846930887', 7)
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

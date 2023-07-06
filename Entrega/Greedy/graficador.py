import networkx as nx
import matplotlib.pyplot as plt

# Crear los grafos
grafo_impares = nx.DiGraph()
grafo_medio = nx.Graph()
grafo_pares = nx.Graph()

# Definir las transiciones
transiciones = [
('304089173', '1303455737', 5),
('1540383427', '304089173', 0),
('1365180541', '1540383427', 3),
('1967513927', '1365180541', 12),
('2044897763', '1967513927', 17),
('1102520059', '2044897763', 9),
('783368691', '1102520059', 1),
('1350490027', '783368691', 7),
('1025202363', '1350490027', 16),
('1189641421', '1025202363', 16),
('596516649', '1189641421', 15),
('1649760493', '596516649', 18),
('719885387', '1649760493', 12),
('424238335', '719885387', 14),
('1957747793', '424238335', 20),
('1714636915', '1957747793', 10),
('1681692777', '1714636915', 20),
('846930887', '1681692777', 2),
('1804289383', '846930887', 2),
('846930887', '1714636915', 10),
('1681692777', '1957747793', 14),
('1714636915', '424238335', 12),
('521595368', '35005210', 17),
('294702566', '35005210', 7),
('1726956428', '294702566', 8),
('336465782', '521595368', 11),
('861021530', '35005210', 1),
('278722862', '521595368', 9),
('233665122', '278722862', 11),
('2145174066', '233665122', 17),
('468703134', '2145174066', 19),
('294702566', '861021530', 17),
('35005210', '233665122', 3),
('1714636915', '336465782', -4),
('1714636915', '2145174066', -28),
('1714636915', '233665122', -26),
('1714636915', '521595368', -27),
('1350490027', '336465782', 0),
('1350490027', '2145174066', 27),
('1350490027', '233665122', 20),
('1350490027', '521595368', 14),
('2044897763', '336465782', 25),
('2044897763', '2145174066', 30),
('2044897763', '233665122', 16),
('2044897763', '521595368', 22),
('1303455737', '336465782', -21),
('1303455737', '2145174066', 6),
('1303455737', '233665122', 17),
('1303455737', '521595368', 20),
('783368691', '336465782', -17),
('783368691', '2145174066', 16),
('783368691', '233665122', 18),
('783368691', '521595368', 5),
('1365180541', '336465782', -25),
('1365180541', '2145174066', 7),
('1365180541', '233665122', 27),
('1365180541', '521595368', 11),
('596516649', '336465782', 20),
('596516649', '2145174066', 14),
('596516649', '233665122', 24),
('596516649', '521595368', -6),
('719885387', '336465782', -12),
('719885387', '2145174066', -21),
('719885387', '233665122', -3),
('719885387', '521595368', -20),
('1967513927', '336465782', -27),
('1967513927', '2145174066', -28),
('1967513927', '233665122', 15),
('1967513927', '521595368', 0),
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

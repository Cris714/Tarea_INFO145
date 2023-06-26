import matplotlib.pyplot as plt

data = {
    (5, 2, 0): [150, 5163.33],
    (5, 3, 0): [120, 4073.33],
    (10, 2, 0): [240, 5546.67],
    (10, 3, 0): [186.67, 4713.33],

    (20, 2, 0): [303.33, 7836.33],
    (20, 3, 0): [253.33, 6266.67],

    (30, 2, 0): [370, 9330],
    (30, 3, 0): [393.33, 11163],
    (40, 2, 0): [600, 15390],
    (40, 3, 0): [393.33, 12900]
}

base_values_p2 = [data[key][0] for key in data if key[1] == 2]
menor_camino_values_p2 = [data[key][1] for key in data if key[1] == 2]
base_values_p3 = [data[key][0] for key in data if key[1] == 3]
menor_camino_values_p3 = [data[key][1] for key in data if key[1] == 3]

x_labels_p2 = [f"({key[0]}, {key[1]}, {key[2]})" for key in data if key[1] == 2]
x_labels_p3 = [f"({key[0]}, {key[1]}, {key[2]})" for key in data if key[1] == 3]

# Gráfico de líneas para Escalera64 (Base) y Escalera64 (Menor camino) con p = 2
plt.figure(figsize=(10, 6))
plt.plot(x_labels_p2, base_values_p2, marker='o', label='Escalera64 (Base) - p = 2')
plt.plot(x_labels_p2, menor_camino_values_p2, marker='o', label='Escalera64 (Menor camino) - p = 2')
plt.xticks(rotation=90)
plt.xlabel('(n, p, r)')
plt.ylabel('Valor')
plt.title('Valores de Escalera64 (Base) y Escalera64 (Menor camino) con r = 0 y p = 2')
plt.legend()
plt.show()

# Gráfico de líneas para Escalera64 (Base) y Escalera64 (Menor camino) con p = 3
plt.figure(figsize=(10, 6))
plt.plot(x_labels_p3, base_values_p3, marker='o', label='Escalera64 (Base) - p = 3')
plt.plot(x_labels_p3, menor_camino_values_p3, marker='o', label='Escalera64 (Menor camino) - p = 3')
plt.xticks(rotation=90)
plt.xlabel('(n, p, r)')
plt.ylabel('Valor')
plt.title('Valores de Escalera64 (Base) y Escalera64 (Menor camino) con r = 0 y p = 3')
plt.legend()
plt.show()

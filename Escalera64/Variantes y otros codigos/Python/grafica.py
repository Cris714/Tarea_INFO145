import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Datos proporcionados
data = {
    (5, 2, 0): [236.67, 150, 10326.67, 5163.33],
    (5, 2, 1): [116.67, 200, 5710, 4613.33],
    (5, 2, 2): [83.33, 163.33, 4633, 4400],
    (5, 3, 0): [143.33, 120, 6429.67, 4073.33],
    (5, 3, 1): [116.67, 136.67, 5223.33, 3706.33],
    (5, 3, 2): [93.33, 136.67, 4616.33, 3316.67],
    (10, 2, 0): [786.67, 240, 52649.67, 5546.67],
    (10, 2, 2): [570, 333.33, 15473, 4783.33],
    (10, 2, 4): [143.33, 286.67, 13460, 4416.67],
    (10, 3, 0): [393.33, 186.67, 20050.33, 4713.33],
    (10, 3, 2): [326.67, 273.33, 10063, 3083.33],
    (10, 3, 4): [140.67, 243.33, 5426.67, 4330],
    (10, 4, 0): [3070, 263.33, 156332, 6296.67],
    (10, 4, 2): [720, 366.67, 22469.33, 5400],
    (10, 4, 4): [163.33, 360, 9263.33, 4290],
    (20, 2, 0): [169839, 303.33, 15288484.33, 7836.33],
    (20, 2, 3): [14776.67, 453.33, 745053.67, 7206.33],
    (20, 2, 9): [636.67, 416.67, 17666.67, 5693.33],
    (20, 3, 0): [9006.67, 253.33, 636491.67, 6266.67],
    (20, 3, 3): [1810, 346.67, 76539.33, 6590],
    (20, 3, 9): [236.67, 410, 8783.33, 5290],
    (20, 4, 0): [2460, 276.67, 152693.33, 5816.67],
    (20, 4, 3): [763.33, 386.67, 47107.33, 5400],
    (20, 4, 9): [163.33, 360, 9263.33, 4290],
    (30, 2, 0): [51769209, 370, 5498334283, 9330],
    (30, 3, 0): [521842, 393.33, 32523518.33, 14999.67],
    (30, 4, 0): [59779.33, 276.67, 3702982, 11470],
    (40, 2, 0): [15486226646, 600, 15486226646, 15390],
    (40, 3, 0): [28798677.33, 393.33, 1748019668.33, 12900],
    (40, 4, 0): [1636033, 330, 102117793.67, 13140],
    (40, 5, 0): [382953.33, 333.33, 18611181, 13200]
}

# Preparar los datos para el gráfico
n_values = np.array([key[0] for key in data.keys()])
p_values = np.array([key[1] for key in data.keys()])
r_values = np.array([key[2] for key in data.keys()])
fb_values = np.array([value[0] for value in data.values()])
eb_values = np.array([value[1] for value in data.values()])
gc_values = np.array([value[2] for value in data.values()])
mc_values = np.array([value[3] for value in data.values()])

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Rango de valores para el plano
n_range = np.linspace(min(n_values), max(n_values), 100)
p_range = np.linspace(min(p_values), max(p_values), 100)
n_grid, p_grid = np.meshgrid(n_range, p_range)

# Interpolar los valores para el plano
fb_grid = griddata((n_values, p_values), fb_values, (n_grid, p_grid), method='linear')
eb_grid = griddata((n_values, p_values), eb_values, (n_grid, p_grid), method='linear')
gc_grid = griddata((n_values, p_values), gc_values, (n_grid, p_grid), method='linear')
mc_grid = griddata((n_values, p_values), mc_values, (n_grid, p_grid), method='linear')

# Crear el plano del gráfico 3D
ax.plot_surface(n_grid, p_grid, fb_grid, alpha=1, cmap='Blues')
ax.plot_surface(n_grid, p_grid, eb_grid, alpha=1, cmap='Reds')
ax.plot_surface(n_grid, p_grid, gc_grid, alpha=0.6, cmap='Greens')
ax.plot_surface(n_grid, p_grid, mc_grid, alpha=1, cmap='Oranges')

# Scatter plot para los puntos de datos
ax.scatter(n_values, p_values, fb_values, c='blue', marker='o', label='Fuerza Bruta')
ax.scatter(n_values, p_values, eb_values, c='red', marker='o', label='Escalera64 (Base)')
ax.scatter(n_values, p_values, gc_values, c='green', marker='o', label='Escalera64 (Guardar soluciones)')
ax.scatter(n_values, p_values, mc_values, c='orange', marker='o', label='Escalera64 (Mejor solucion)')

# Etiquetas de los ejes
ax.set_xlabel('n')
ax.set_ylabel('p')
ax.set_zlabel('Tiempo [ns]')

# Leyenda
ax.legend()

# Mostrar el gráfico
plt.show()

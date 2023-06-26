import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def nlogn(x, c):
    return c * x * np.log2(x)

# Datos primer gráfico
n_values1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
times1 = [4110, 4170, 5270, 6089, 12530, 20500, 35670, 73889, 165209, 351777, 783284, 1643967, 3729250]

# Ajuste de curva primer gráfico
popt1, pcov1 = curve_fit(nlogn, n_values1, times1)
c1 = popt1[0]

# Datos segundo gráfico
n_values2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
times2 = [120, 150, 200, 290, 350, 670, 1290, 2760, 5650, 13170, 28189, 63579, 139459]

# Gráfico combinado
plt.figure(figsize=(10, 6))
plt.plot(n_values1, times1, marker='o', linestyle='-', label='escalera64 (Mejor Solucion)')
plt.plot(n_values1, nlogn(np.array(n_values1), c1), linestyle='--', label=f'{c1:.2f}nlog(n)')
plt.plot(n_values2, times2, marker='o', linestyle='-', label='escalera64 (Base)')
plt.xlabel('n')
plt.ylabel('Tiempo [ns]')
plt.title('Comparación de Complejidades')
plt.legend()
plt.show()

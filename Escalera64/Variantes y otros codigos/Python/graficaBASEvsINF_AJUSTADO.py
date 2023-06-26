import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def nlogn(x, c):
    return c * x * np.log2(x)

# Datos del primer gráfico
n_values_1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
times_1 = [4110, 4170, 5270, 6089, 12530, 20500, 35670, 73889, 165209, 351777, 783284, 1643967, 3729250]

# Ajuste de curva del primer gráfico
popt_1, pcov_1 = curve_fit(nlogn, n_values_1, times_1)
c_1 = popt_1[0]

# Datos del segundo gráfico
n_values_2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
times_2 = [120, 150, 200, 290, 350, 670, 1290, 2760, 5650, 13170, 28189, 63579, 139459]

# Multiplicar los tiempos del segundo gráfico por la constante
times_2_adjusted = [27 * t for t in times_2]

# Gráfico combinado
plt.figure(figsize=(10, 6))
plt.plot(n_values_1, times_1, marker='o', linestyle='-', label='escalera64(Mejor solucion)')
plt.plot(n_values_1, nlogn(np.array(n_values_1), c_1), linestyle='--', label=f'{c_1:.2f}nlog(n)')
plt.plot(n_values_2, times_2_adjusted, marker='o', linestyle='-', label=f'escalera64 (BASE) (Ajustado x{27:.2f})')
plt.xlabel('n')
plt.ylabel('Tiempo [ns]')
plt.title('Comparación de Complejidades')
plt.legend()
plt.show()

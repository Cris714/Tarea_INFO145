import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def nlogn(x, c):
    return c * x * np.log2(x)

# Datos
n_values = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
times = [4110, 4170, 5270, 6089, 12530, 20500, 35670, 73889, 165209, 351777, 783284, 1643967, 3729250, 7569969, 16296999, 35508073, 74887659]

# Ajuste de curva
popt, pcov = curve_fit(nlogn, n_values, times)
c = popt[0]

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-', label='escalera64 (Mejor solucion)')
plt.plot(n_values, nlogn(np.array(n_values), c), linestyle='--', label=f'{c:.2f}nlog(n)')
plt.xlabel('n')
plt.ylabel('Tiempo [ns]')
plt.title('Complejidad del algoritmo')
plt.legend()
plt.show()

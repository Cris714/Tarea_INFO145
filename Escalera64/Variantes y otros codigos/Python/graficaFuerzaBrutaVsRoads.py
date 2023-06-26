import numpy as np
import matplotlib.pyplot as plt

# Datos del primer conjunto
n_values_1 = [2, 4, 8, 16, 32]
times_1 = [70, 130, 410, 17670, 171077665]

# Datos del segundo conjunto
n_values_2 = [2, 4, 8, 16, 30]
times_2 = [6030, 7690, 43830, 1227920, 6121026531]

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(n_values_1, times_1, marker='o', linestyle='-', label='Fuerza Bruta')
plt.plot(n_values_2, times_2, marker='o', linestyle='-', label='PD (Todas las soluciones)')
plt.axvline(x=30, color='r', linestyle='--', label='n=30')
plt.xlabel('n')
plt.ylabel('Tiempo [ns]')
plt.title('Comparación de Tiempos de Ejecución')
plt.legend()
plt.xscale('log', base=2)
plt.yscale('log', base=10)
plt.show()

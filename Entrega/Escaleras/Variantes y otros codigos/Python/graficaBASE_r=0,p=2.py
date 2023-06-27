import numpy as np
import matplotlib.pyplot as plt

n_values = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
times = [120, 150, 200, 290, 350, 670, 1290, 2760, 5650, 13170, 28189, 63579, 139459]

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, marker='o', linestyle='-', label='escalera64 (Base)')
plt.xlabel('n')
plt.ylabel('Tiempo [ns]')
plt.title('Tiempos en función de n')
plt.legend()
plt.show()
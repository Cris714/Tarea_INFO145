import matplotlib.pyplot as plt

# Datos para el primer gráfico
r_values = [0, 3, 9]
fuerza_bruta = [169839, 14776.67, 636.67]
escalera_base = [303.33, 453.33, 416.67]
escalera_guardar_caminos = [15288484.33, 745053.67, 17666.67]
escalera_menor_camino = [7836.33, 7206.33, 5693.33]

# Generar el primer gráfico
plt.figure(1)
plt.plot(r_values, fuerza_bruta, marker='o', label='Fuerza Bruta')
plt.plot(r_values, escalera_base, marker='o', label='Escalera64 (Base)')
plt.plot(r_values, escalera_guardar_caminos, marker='o', label='Escalera64 (Guardar caminos)')
plt.plot(r_values, escalera_menor_camino, marker='o', label='Escalera64 (Menor camino)')

plt.xlabel('r')
plt.ylabel('Tiempo (nanosegundos)')
plt.title('Comparación de tiempos en función de r')
plt.legend()

# Datos para el segundo gráfico (excluyendo Escalera64 Guardar caminos)
escalera_guardar_caminos_excluido = [None, None, None]

# Generar el segundo gráfico
plt.figure(2)
plt.plot(r_values, fuerza_bruta, marker='o', label='Fuerza Bruta')
plt.plot(r_values, escalera_base, marker='o', label='Escalera64 (Base)')
plt.plot(r_values, escalera_menor_camino, marker='o', label='Escalera64 (Menor camino)')

plt.xlabel('r')
plt.ylabel('Tiempo (nanosegundos)')
plt.title('Comparación de tiempos en función de r (sin Escalera64 Guardar caminos)')
plt.legend()

# Mostrar ambos gráficos
plt.show()

import csv
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
with open('earth_sun_distance_monthly_2000_2020.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la primera fila (encabezado)
    data = list(reader)

# Convertir las cadenas de texto en números
data = [[int(row[0]), float(row[1])] for row in data]

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 5))

# Graficar la distancia Tierra-Sol promedio mensual
x = [row[0] for row in data]
y = [row[1] for row in data]
ax.plot(x, y)

# Encontrar los perihelios y afelios en el período
perihelios = []
afelios = []
for i in range(1, len(data) - 1):
    if y[i] < y[i-1] and y[i] < y[i+1]:
        perihelios.append(x[i])
    elif y[i] > y[i-1] and y[i] > y[i+1]:
        afelios.append(x[i])

# Graficar los perihelios y afelios
for p in perihelios:
    ax.axvline(x=p, color='red', linestyle='--')
for a in afelios:
    ax.axvline(x=a, color='blue', linestyle='--')

# Etiquetas y título
ax.set_xlabel('Días del año')
ax.set_ylabel('Distancia Tierra-Sol (km)')
ax.set_title('Perihelios y afelios 2000-2020')

# Mostrar la gráfica
plt.show()
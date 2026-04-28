# Repaso para junio 53

# (Ejemplo de examen de mínimos, 5/12)

# 53.- Pide al usuario que introduzca 10 números reales, guárdalos en 
# una lista y luego muestra, del último al primero, todos los que eran 
# positivos, cada uno en una línea.

# Versión 2: recorre del último al primero, reales
# (lo que se pedía)

# Preparamos una lista vacía
datos = [ ]

# Pedimos 10 datos y los vamos añadiendo
for i in range(10):
    datos.append(float(input("Dame un dato: ")))

# Recorremos los 10 datos y mostramos los positivos
# (Versión 2: de fin a principio)
for i in range(9, -1, -1):
    if datos[i] > 0:
        print(datos[i])

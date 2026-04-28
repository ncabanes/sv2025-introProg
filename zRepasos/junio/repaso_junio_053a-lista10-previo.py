# Repaso para junio 53

# (Ejemplo de examen de mínimos, 5/12)

# 53.- Pide al usuario que introduzca 10 números reales, guárdalos en 
# una lista y luego muestra, del último al primero, todos los que eran 
# positivos, cada uno en una línea.

# Versión 1: recorre del primero al último, enteros
# (algo más sencillo que lo que realmente se pide)

# Preparamos una lista vacía
datos = [ ]

# Pedimos 10 datos (enteros) y los vamos añadiendo
for i in range(10):
    dato = int(input("Dame un dato: "))
    datos.append(dato)

# Recorremos los 10 datos y mostramos los positivos
# (Versión 1: de principio a fin)
for n in datos:
    if n > 0:
        print(n)

# Rectángulo hueco

filas = int(input("Filas?" ))
columnas = int(input("Columnas?" ))

for fila in range(0, filas):
    for columna in range(0, columnas):
        if fila == 0 or fila == filas-1 or columna == 0 or columna == columnas-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

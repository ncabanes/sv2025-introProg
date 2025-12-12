# 2C - 1ev - Ejercicio 5

# 5. Crea una función "escribir_triang_decrec_derecha", que escriba un triángulo 
# decreciente alineado a la derecha, con el tamaño que se indique como parámetro. 
# Por ejemplo, para tamaño 4 debería dibujar algo como:
# 
# ****
#  ***
#   **
#    *

# Planteamiento 1, contando espacios (creciente) y deduciendo asteriscos

def escribir_triang_decrec_derecha(tamano: int) -> None:
    for espacios in range(0, tamano):
        asteriscos = tamano - espacios
        print(" " * espacios + "*" * asteriscos)

# Programa de prueba
ancho = int(input("Introduce el tamaño del triángulo: "))
escribir_triang_decrec_derecha(ancho)

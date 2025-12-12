# 2A - 1ev - Ejercicio 5

# 5. Crea una función "escribir_triang_creciente", que escriba un triángulo 
# creciente, con el tamaño de la base que se indique como parámetro. Por ejemplo, 
# para tamaño 7 debería dibujar algo como:
# 
#    *
#   ***
#  *****
# *******
# 
# Y para tamaño 6 sería:
# 
#    **
#   ****
#  ******


def escribir_triang_creciente(base):
    # Calculamos la altura (número de filas)
    altura = (base + 1) // 2
    
    # Primera fila: espacios y asteriscos iniciales
    if base % 2 != 0:
        asteriscos = 1
        espacios = (base - 1) // 2
    else:
        asteriscos = 2
        espacios = (base - 2) // 2
    
    # Bucle que avanza fila a fila
    for _ in range(altura):
        print(" " * espacios + "*" * asteriscos)
        espacios -= 1
        asteriscos += 2

# Programa de prueba
t = int(input("Introduce el tamaño de la base: "))
escribir_triang_creciente(t)

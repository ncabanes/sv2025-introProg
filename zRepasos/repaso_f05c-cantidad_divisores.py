"""
3. Crea una función "cantidad_divisores", que devuelva
la cantidad de divisores del número entero que se le pase
como parámetro. Por ejemplo, si n = 8, la función debería
devolver 4 (porque el número 8 tiene 4 divisores: 1, 2, 4, 8).
Pruébala desde el cuerpo del programa.
"""

def cantidad_divisores(n):
    cantidad = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            cantidad += 1
    return cantidad

print("Divisores del 8:", cantidad_divisores(8))

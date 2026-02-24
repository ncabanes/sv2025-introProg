"""
3. Crea una función "sumar_pares_hasta", que devuelva la suma
de los números pares que hasta el número n, que se indicará
como parámetro, empezando en 1 (ambos incluidos). Por ejemplo,
si n = 8, la función debería devolver 20 (porque entre el 1 y
el 8 están los pares 2, 4, 6, 8, que suman 20). Pruébala desde
el cuerpo del programa.
"""

# Versión 1, recorriendo todos los números

def sumar_pares_hasta(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

print(sumar_pares_hasta(8))

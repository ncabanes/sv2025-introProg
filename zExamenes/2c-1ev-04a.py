# 2C - 1ev - Ejercicio 4

# 4. Crea una función "menor_de_4", que reciba como parámetros cuatro números 
# reales, y devuelva el valor del menor de ellos. Crea un programa de prueba que 
# pida al usuario 4 datos y muestre el menor de ellos. Por ejemplo, si los 
# números son 3 2 2 4, la respuesta debería ser 2.

# Planteamiento 1: comparando cada uno con todos

def menor_de_4(a: float, b: float, c: float, d: float) -> float:
    if a <= b and a <= c and a <= d:
        return a
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    else:
        return d

# Programa de prueba
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))
n4 = float(input("Introduce el cuarto número: "))

print("El menor es:", menor_de_4(n1, n2, n3, n4))

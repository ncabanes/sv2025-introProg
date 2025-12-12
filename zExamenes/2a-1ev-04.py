# 2A - 1ev - Ejercicio 4

# 4. Crea una función "media_de_5", que reciba como parámetros cinco números 
# reales, y devuelva su media. Crea un programa de prueba que pida al usuario 5 
# datos y muestre su media, ayudándose de esta función.

def media_de_5(a: float, b: float, c: float, d: float, e: float) -> float:
    return (a + b + c + d + e) / 5

# Programa de prueba
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))
n4 = float(input("Introduce el cuarto número: "))
n5 = float(input("Introduce el quinto número: "))

print("La media es:", media_de_5(n1, n2, n3, n4, n5))

# 2C - 1ev - Ejercicio 1

# 1. Crea un programa que pida al usuario dos números y muestre todos los que hay 
# entre el primero y el segundo, ambos incluidos, indicando si son múltiplos de 3 
# y/o de 7. Por ejemplo, si los números son 18 y 22, la respuesta debería ser:
# 
# 18
# Múltiplo de 3
# 19
# 20
# 21
# Múltiplo de 3
# Múltiplo de 7
# 22

inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

for i in range(inicio, fin + 1):
    print(i)
    if i % 3 == 0:
        print("Múltiplo de 3")
    if i % 7 == 0:
        print("Múltiplo de 7")

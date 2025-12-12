# 2A - 1ev - Ejercicio 1

# 1. Crea un programa que pida al usuario dos números y muestre todos los que hay 
# entre el menor de ellos y el mayor de ellos que sean múltiplos de 3 y/o de 7. 
# Por ejemplo, si el usuario introduce los números 12 y 7, la respuesta debería 
# ser "7 9 12 " (en la misma línea, separados por un espacio en blanco).

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

if a < b:
    menor = a
    mayor = b
else:
    menor = b
    mayor = a

for num in range(menor, mayor + 1):
    if num % 3 == 0 or num % 7 == 0:
        print(num, end=" ")

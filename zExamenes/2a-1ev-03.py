# 2A - 1ev - Ejercicio 3

# 3. Pide un número entero al usuario. Luego, pídele otros 5 números enteros, y 
# para cada uno de ellos deberás decirle si es múltiplo del primero o no. Por 
# ejemplo, si el número inicial es 4 y los cinco números de prueba son 12, 11, 
# 16, 13, 100, la respuesta debería ser:
# 
# Sí
# No
# Sí
# No
# Sí


divisor = int(input("Introduce el número base: "))

for i in range(5):
    num = int(input("Dime un número: "))
    if num % divisor == 0:
        print("Sí")
    else:
        print("No")

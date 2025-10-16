# Crea un programa que pida al usuario un número entero 
# y muestre sus divisores.

print("Número del que quieres ver los divisores?")
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

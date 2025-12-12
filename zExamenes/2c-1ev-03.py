# 2C - 1ev - Ejercicio 3

# 3. Pide diez números enteros al usuario. Luego respóndele cuántos de 
# ellos eran múltiplos de 5.

contador = 0
for i in range(10):
    num = int(input("Dime un número: "))
    if num % 5 == 0:
        contador += 1

print("Múltiplos de 5:", contador)

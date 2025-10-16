# Crea un programa que pida al usuario un número entero 
# y responda si es primo o no.

# Pista: un número es primo si tiene exactamente 2 divisores
# (si sólo es divisible por el 1 y por sí mismo).

cantidadDeDivisores = 0

print("Número del que quieres ver los divisores?")
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        #print(i, end=" ")
        cantidadDeDivisores += 1

#print()
#print(cantidadDeDivisores)
if cantidadDeDivisores == 2:
    print("Es primo")
else:
    print("No es primo")

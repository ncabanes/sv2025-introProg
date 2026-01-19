# Pide al usuario números enteros, 
# hasta que introduzca 0 para terminar. 
# Luego dile cuántos números distintos 
# ha introducido y muestra todos esos 
# números (sin duplicados).

numeros = set() # Usamos un conjunto

numero = int(input("Dime un número: "))
while numero != 0:
    numeros.add(numero)
    numero = int(input("Dime un número: "))

print("Cantidad: ", len(numeros))
print("Datos: ", numeros)

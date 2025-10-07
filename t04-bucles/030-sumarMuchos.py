# 30. Suma de muchos números

# Pide al usuario números enteros, hasta que introduzca
# un 0, y entonces dile la suma de todos ellos, así:
# 
# Número? 21
# Número? 15
# Número? -5
# Número? 3
# Número? 0
# Su suma es 34

suma = 0
n = int(input("Número? "))
while n != 0:
    suma += n
    n = int(input("Número? "))

print("Su suma es", suma)

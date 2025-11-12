# Inicial y nombre al revés

nombre = input("Nombre? ")

print("Tu inicial es", nombre[0])

print("Tu nombre al revés es ", end="")
for i in range(len(nombre)-1, -1, -1):
    print(nombre[i], end="")

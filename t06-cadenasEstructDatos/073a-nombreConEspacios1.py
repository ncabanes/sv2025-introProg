# Nombre con espacios intermedios

# Versión 1: con "range"

nombre = input("Nombre? ")

print("Tu nombre con espacios es ", end="")
for i in range(len(nombre)):
    print(nombre[i], end=" ")

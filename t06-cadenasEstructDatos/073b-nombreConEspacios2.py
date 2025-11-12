# Nombre con espacios intermedios

# Versión 2: "for" para extraer letras

nombre = input("Nombre? ")

print("Tu nombre con espacios es ", end="")
for letra in nombre:
    print(letra, end=" ")

# for i in range(len(nombre)):
#    print(nombre[i], end=" ")

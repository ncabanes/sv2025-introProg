# Repaso para junio 72

# 72.- Crea un programa que prepare dos listas vacías. Preguntará al 
# usuario una palabra a añadir (por ejemplo, "hola") y un número de lista 
# (1 o 2), y añadirá esa palabra en esa lista. Se repetirá hasta que el 
# usuario introduzca una cadena vacía. A continuación, mostrará el 
# contenido de la lista más larga.

lista1 = [ ]
lista2 = [ ]

palabra = input("Dime una palabra: ")
while palabra != "":
    numero_lista = input("¿En la lista 1 o 2? ")
    if numero_lista == "1":
        lista1.append(palabra)
    else:
        lista2.append(palabra)
    palabra = input("Dime una palabra: ")

print("La lista más larga tiene...")
if len(lista1) > len(lista2):
    # print(lista1)
    for palabra in lista1:
        print(palabra)
else:
    # print(lista2)
    for palabra in lista2:
        print(palabra)

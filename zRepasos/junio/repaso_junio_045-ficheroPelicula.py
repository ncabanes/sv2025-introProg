# 45.- Crea (por ejemplo, usando el "bloc de notas" de Windows) un 
# fichero de texto llamado "peliculas.txt", que contenga en cada línea el 
# título de una película. Luego haz un programa que le pregunte al 
# usuario el título de una película y le responda si aparece entre 
# nuestros datos (recorriendo ese fichero línea a línea).

titulo = input("Qué titulo buscamos? ")

encontrado = False
fichero = open("peliculas.txt", "r")
for linea in fichero:
    if linea.rstrip() == titulo:
        encontrado = True
fichero.close()

if encontrado:
    print("Existe!")
else:
    print("No existe!")

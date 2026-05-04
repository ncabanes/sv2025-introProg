# Repaso para junio 6'

# (Ejemplo de examen de mínimos, 12/12)

# 60.- Pide al usuario que introduzca cadenas de texto, tantas como 
# quiera. Cuando pulse Intro sin teclear nada, terminará la introducción 
# de datos y guardarás todas las cadenas, en mayúsculas y en orden 
# inverso (de la última a la primera) en un fichero llamado "textos.txt".

# Primera aproximación, de principio a fin

textos =  [ ]
frase = input("Dime un texto: ")
while frase != "":
    textos.append(frase)
    frase = input("Dime otro texto: ")

fichero = open("textos.txt", "w")
for texto in textos:
    fichero.write(texto+"\n")
fichero.close()

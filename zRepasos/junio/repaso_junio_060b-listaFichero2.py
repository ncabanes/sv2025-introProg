# Repaso para junio 6'

# (Ejemplo de examen de mínimos, 12/12)

# 60.- Pide al usuario que introduzca cadenas de texto, tantas como 
# quiera. Cuando pulse Intro sin teclear nada, terminará la introducción 
# de datos y guardarás todas las cadenas, en mayúsculas y en orden 
# inverso (de la última a la primera) en un fichero llamado "textos.txt".

# Segunda aproximación, de fin a principio, en mayúsculas

textos =  [ ]
frase = input("Dime un texto: ")
while frase != "":
    textos.append(frase)
    frase = input("Dime otro texto: ")

fichero = open("textos.txt", "w")
for i in range(len(textos)-1, -1, -1):
    fichero.write(textos[i].upper()+"\n")
fichero.close()

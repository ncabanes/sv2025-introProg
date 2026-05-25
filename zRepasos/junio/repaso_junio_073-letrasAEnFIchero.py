# Repaso para junio 73

# 73.- Pide al usuario que introduzca el nombre de un fichero de texto 
# y respóndele cuántas letras "a" (en minúsculas) contiene el texto del 
# fichero (no su nombre).

cantidad_a = 0
nombre = input("Nombre del fichero: ")
f = open(nombre, "r")
for linea in f:
    for letra in linea:
        if letra == "a":
            cantidad_a += 1
f.close()
print('Letras "a":', cantidad_a)

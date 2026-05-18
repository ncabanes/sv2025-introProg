# Repaso para junio 63

# 63.- Pide al usuario que introduzca una frase formada por dos 
# palabras de la misma longitud. Si no introduce dos palabras o son de 
# longitud distinta, deberás responderle "Algo falla" y volverle a pedir 
# la frase. Esto debe repetirse hasta que realmente introduzca una frase 
# formada por dos palabras de la misma longitud, y en ese momento 
# escribirás "Perfecto" y finalizará la ejecución.

# Versión previa: pidiendo las dos palabras por separado

palabra1 = input("Dime la primera palabra: ")
palabra2 = input("Dime la segunda palabra, de la misma longitud: ")

while len(palabra1) != len(palabra2):
    print("Algo falla")

    palabra1 = input("Dime la primera palabra: ")
    palabra2 = input("Dime la segunda palabra, de la misma longitud: ")
    
print("Perfecto")

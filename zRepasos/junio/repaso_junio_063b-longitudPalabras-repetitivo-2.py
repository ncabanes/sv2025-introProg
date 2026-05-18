# Repaso para junio 63

# 63.- Pide al usuario que introduzca una frase formada por dos 
# palabras de la misma longitud. Si no introduce dos palabras o son de 
# longitud distinta, deberás responderle "Algo falla" y volverle a pedir 
# la frase. Esto debe repetirse hasta que realmente introduzca una frase 
# formada por dos palabras de la misma longitud, y en ese momento 
# escribirás "Perfecto" y finalizará la ejecución.

# Versión correcta: una frase que se parte con "split()"

frase = input("Dime dos palabras de la misma longitud: ")
trozos = frase.split()
palabra1 = trozos[0]
palabra2 = trozos[1]

while len(palabra1) != len(palabra2):
    print("Algo falla")

    frase = input("Dime dos palabras de la misma longitud: ")
    trozos = frase.split()
    palabra1 = trozos[0]
    palabra2 = trozos[1]
    
print("Perfecto")

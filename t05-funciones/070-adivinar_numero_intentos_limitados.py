# Crea un programa en el que el usuario deba adivinar un número (prefijado). 
# Será un número del 1 al 1000 y tendrá un máximo de 9 intentos. 
# Tras cada intento deberás avisarle en caso de que se pase o se quede corto.

adivinar = 123
acertado = False
intentos = 0
max_intentos = 9

while not acertado and intentos < max_intentos:
    numero = int(input("Dime un número: "))
    intentos += 1
    
    if numero > adivinar:
        print("Te has pasado")
        print("Te quedan",max_intentos-intentos,"intentos")
    elif numero < adivinar:
        print("Te has quedado corto")
        print("Te quedan",max_intentos-intentos,"intentos")
    else:
        acertado = True

if acertado:
    print("Has acertado")
else:
    print("Lo siento, era:", adivinar)

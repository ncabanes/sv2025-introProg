# Crea un programa en el que el usuario deba adivinar un número (prefijado),
# con una cantidad ilimitada de oportunidades. Tras cada intento deberás 
# avisarle en caso de que se pase o se quede corto.

# Aproximación 1 (incorrecta): bucle sin fin

adivinar = 123

numero = int(input("Dime un número: "))

while numero != adivinar:
    if numero > adivinar:
        print("Te has pasado")
        numero = int(input("Dime un número: "))
    elif numero < adivinar:
        print("Te has quedado corto")
        numero = int(input("Dime un número: "))
    else:
        print("Has acertado")

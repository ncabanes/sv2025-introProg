# Crea un programa en el que el usuario deba adivinar un número (prefijado),
# con una cantidad ilimitada de oportunidades. Tras cada intento deberás 
# avisarle en caso de que se pase o se quede corto.

# Versión 2 (correcta 1): pide 2 veces

adivinar = 123

numero = int(input("Dime un número: "))

while numero != adivinar:
    if numero > adivinar:
        print("Te has pasado")
    elif numero < adivinar:
        print("Te has quedado corto")

    numero = int(input("Dime un número: "))

print("Has acertado")

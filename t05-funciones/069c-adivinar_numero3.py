# Crea un programa en el que el usuario deba adivinar un número (prefijado),
# con una cantidad ilimitada de oportunidades. Tras cada intento deberás 
# avisarle en caso de que se pase o se quede corto.

# Versión 3 (correcta 2): booleano de control

adivinar = 123
acertado = False

while not acertado:
    numero = int(input("Dime un número: "))
    
    if numero > adivinar:
        print("Te has pasado")
    elif numero < adivinar:
        print("Te has quedado corto")
    else:
        acertado = True

print("Has acertado")

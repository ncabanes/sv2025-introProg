# 2C - 1ev - Ejercicio 2

# 2. Crea un programa que pida al usuario una nota numérica (entera, del 0 al 10) 
# y que responda el nombre de esa nota en el sistema clásico español (9 y 10 = 
# Sobresaliente, 7 y 8 = Notable, 6 = Bien, 5 = Suficiente, 0 a 4 = Suspenso).

nota = int(input("Introduce una nota (0-10): "))

if nota == 9 or nota == 10:
    print("Sobresaliente")
elif nota == 7 or nota == 8:
    print("Notable")
elif nota == 6:
    print("Bien")
elif nota == 5:
    print("Suficiente")
elif nota >= 0 and nota <= 4:
    print("Suspenso")
else:
    print("Nota no válida")

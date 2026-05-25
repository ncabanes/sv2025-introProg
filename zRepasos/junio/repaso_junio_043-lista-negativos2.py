# 43.- Haz una versión mejorada del ejercicio anterior: Crea una lista 
# vacía. Pide al usuario que introduzca números enteros, ya sean 
# positivos o negativos, usando el 0 como señal de que quiere terminar, y 
# añádelos a la lista. Finalmente, muestra los datos negativos que había 
# en la lista, en una misma línea, separados por espacios, o bien el 
# texto "No había negativos" si corresponde.

numeros = [ ]

n = int(input("Dime un número: "))
while n != 0:
    numeros.append(n)
    n = int(input("Dime un número: "))

cantidad_negativos = 0
for n in numeros:
    if n < 0 :
        print(n, end=" ")
        cantidad_negativos += 1

if cantidad_negativos == 0:
    print("No había negativos")

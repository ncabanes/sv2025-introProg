# 42.- Crea una lista vacía. Pide al usuario que introduzca números 
# enteros, ya sean positivos o negativos, usando el 0 como señal de que 
# quiere terminar, y añádelos a la lista. Finalmente, muestra los datos 
# negativos que había en la lista.

numeros = [ ]

n = int(input("Dime un número: "))
while n != 0:
    numeros.append(n)
    n = int(input("Dime un número: "))

for n in numeros:
    if n < 0 :
        print(n)

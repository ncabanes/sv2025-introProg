# 41.- Crea una lista vacía. Pide 10 números al usuario, guárdalos en 
# la lista y luego muestra los que están en posiciones impares (el 
# primero, tercero, quinto, séptimo y noveno).

numeros = [ ]

for i in range(10):
    n = int(input("Dime un número: "))
    numeros.append(n)

for i in range(0, 9, 2):
    print(numeros[i])

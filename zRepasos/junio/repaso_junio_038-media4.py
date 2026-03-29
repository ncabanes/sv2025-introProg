# Repaso para junio 38

# 38.- Pide al usuario números reales,
# tantos como desee, hasta que introduzca
# un 0 para terminar, y después muestra
# su media. Debes guardar los datos en
# una lista.

# Pedir datos
lista = [ ]
n = float(input("Dime un número: "))
while n != 0 :
    lista.append(n)
    n = float(input("Dime un número: "))

# Calcular resultados
suma = 0
for dato in lista:
    suma += dato

print("La media es", suma/len(lista))

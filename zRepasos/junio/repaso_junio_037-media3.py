# Repaso para junio 37

# Pide al usuario números reales, tantos
# como desee, hasta que introduzca un 0 para
# terminar. Después, muestra su media, usando
# sólo tres variables: el número que se pide
# al usuario (que siempre se guardará en la
# misma variable), la suma de los datos
# introducidos y la cantidad de datos
# introducidos.

suma = 0
cantidad = 0
n = float(input("Dime un número: "))
while n != 0 :
    suma += n
    cantidad += 1
    n = float(input("Dime un número: "))

print("La media es", suma/cantidad)

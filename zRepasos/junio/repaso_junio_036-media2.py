# Repaso para junio 36

# Pide al usuario 10 números reales y
# luego muestra su media, usando sólo dos
# variables: el número que se pide al
# usuario (que siempre se guardará en
# la misma variable) y la suma de los
# datos introducidos.

suma = 0
for i in range(10):
    n = float(input("Dime un número: "))
    suma += n

print("La media es", suma/10)

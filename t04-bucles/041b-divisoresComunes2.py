# Crea un programa que pida al usuario dos número enteros
# y muestre sus divisores comunes.

# Aproximación 2, mejorada: sólo avanza hasta el menor de los dos.

n1 = int(input("N1?"))
n2 = int(input("N2?"))

menor = n1
if n2 < n1:
    menor = n2

for i in range(1, menor+1):
    if n1 % i == 0 and n2 % i == 0:
        print(i, end=" ")

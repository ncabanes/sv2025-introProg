# Crea un programa que pida al usuario dos número enteros
# y muestre sus divisores comunes.

# Aproximación 1: recorre hasta el primer número
# (quizá dé pasos de más, basta con llegar hasta el menor)

n1 = int(input("N1?"))
n2 = int(input("N2?"))
for i in range(1, n1+1):
    if n1 % i == 0 and n2 % i == 0:
        print(i, end=" ")

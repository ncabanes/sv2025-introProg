# Repaso para junio 15

# 15. Pide al usuario dos números
# y dile cuántos son pares


n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Los dos son pares")
elif n1 % 2 == 0 or n2 % 2 == 0:
    print("Uno es par")
else:
    print("Ninguno es par")

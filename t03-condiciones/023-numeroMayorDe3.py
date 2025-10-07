# Número mayor de 3

n1 = int(input("Dime un numero: "))
n2 = int(input("Dime un otro: "))
n3 = int(input("Dime el ultimo: "))

if n1 >= n2 and n1 >= n3:
    print("El mayor es", n1)
elif n2 >= n1 and n2 >= n3:
    print("El mayor es", n2)
else:
    print("El mayor es", n3)

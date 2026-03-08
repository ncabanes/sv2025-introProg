# Repaso para junio 10

# Prepara un programa que pida al usuario
# dos números enteros y muestre el resultado
# de dividir el primero entre el segundo,
# si el segundo no es 0, o bien el texto
# "No puedo hacer esa división" en caso de
# que el segundo sea 0.

n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))
if n2 != 0:
    division = n1 / n2
    print(n1, "/", n2, "=", division)
else:
    print("No puedo hacer esa división")

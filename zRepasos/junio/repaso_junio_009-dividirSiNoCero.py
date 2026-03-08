# Repaso para junio 09

# Crea un programa que pida al usuario 
# dos números enteros y muestre el resultado 
# de dividir el primero entre el segundo, 
# pero sólo cuando el segundo no sea cero.

n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))
if n2 != 0:
    division = n1 / n2
    print(n1, "/", n2, "=", division)

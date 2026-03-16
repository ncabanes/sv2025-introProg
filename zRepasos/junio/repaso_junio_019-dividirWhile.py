# Repaso para junio 19

# Crea un programa que pida al usuario dos números
# enteros y muestre el resultado de dividir el 
# primero entre el segundo, pero sólo cuando el 
# segundo no sea cero, teniendo en cuenta que 
# quizá se equivoque más de una vez.

n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))
while n2 == 0:
    print("No debe ser cero")
    n2 = int(input("Dime el segundo número: "))
    
division = n1 / n2
print(n1, "/", n2, "=", division)

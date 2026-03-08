# Repaso para junio 13

# Crea un programa que pida al usuario un 
# número entero y le diga si es a la vez par 
# y múltiplo de 3.

n = int(input("Dime un número: "))

if n % 2 == 0 and n % 3 == 0:
    print("Es par y múltiplo de 3")
else:
    print("No es par y múltiplo de 3 a la vez")

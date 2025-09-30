# Ejercicio 17: Positivo, negativo o cero

# Pide un número entero al usuario y respóndele si es positivo, 
# negativo o cero. En esta nueva versión debes emplear "elif".

n = int(input("Dime un número entero: "))
if n > 0:
    print("Es positivo")
elif n < 0:
    print("Es negativo")
else:
    print("Es cero")

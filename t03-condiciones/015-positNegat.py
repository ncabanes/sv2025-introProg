# Ejercicio 15. Positivo, negativo o cero

# Pide un número entero al usuario y respóndele si es positivo, 
# negativo o cero. Debes emplear if + else + if + ...

n = int(input("Dime un número entero: "))
if n > 0:
    print("Es positivo")
else:
    if n < 0:
        print("Es negativo")
    else:
        print("Es cero")

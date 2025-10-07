# 24. Valor absoluto de un número

# Pide al usuario un número y muestra su valor absoluto 
# (si es negativo, deberás multiplicarlo por -1 para 
# que pase a ser positivo)

# Versión 2: comparador al revés, y "-n" en vez de "n * (-1)"

numero = int(input("Dime un numero:"))

if numero < 0:
    print("El valor absoluto es:", -numero)
else:
    print("El valor absoluto es:", numero)
    

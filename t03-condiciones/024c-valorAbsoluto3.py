# 24. Valor absoluto de un número

# Pide al usuario un número y muestra su valor absoluto 
# (si es negativo, deberás multiplicarlo por -1 para 
# que pase a ser positivo)

# Versión 3: con una variable auxiliar

numero = int(input("Dime un numero:"))

if numero < 0:
    valorAbsoluto = -numero
else:
    valorAbsoluto = numero

print("El valor absoluto es:", valorAbsoluto)
    

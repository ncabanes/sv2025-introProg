# 27. Dividir si no es cero

# Pide dos números reales al usuario y muestra su división.
# Si el divisor que introduce es 0, debes avisarle y volvérselo
# a perdir tantas veces como sea necesario.

dividendo = float(input("Dividendo? "))
divisor = float(input("Divisor? "))

while divisor == 0:
    print("No puede ser cero")
    divisor = float(input("Divisor? "))

print("La división es ", dividendo / divisor)


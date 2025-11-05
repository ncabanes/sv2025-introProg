# Ejercicio 62. Función  area_circulo

# Crea una función "area_circulo". que devuelva el área de un círculo 
# a partir de su radio, que recibirá como parámetro

def area_circulo(radio: float) -> float:
    return 3.1415926535 * radio * radio

r = float(input("Dime el radio: "))
print( area_circulo(r) )

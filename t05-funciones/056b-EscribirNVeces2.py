# Crea una función "EscribirNVeces", que reciba como parámetros un texto
# y un número entero y escriba, en una misma línea, ese texto repetido esa
# cantidad de veces.

# Versión 2: con "type hinting"

def EscribirNVeces(texto: str, cantidad: int):
    for i in range(cantidad):
        print(texto)

EscribirNVeces("Hola", 3)
EscribirNVeces("###", 5)

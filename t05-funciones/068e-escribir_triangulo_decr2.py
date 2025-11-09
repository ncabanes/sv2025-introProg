# Crea una función "escribir_triángulo_decr", que reciba un 
# tamaño y un símbolo, y escriba un triángulo alineado a la 
# izquierda decreciente, algo como:

# ****
# ***
# **
# *

# Versión decreciente 2: multiplicando el símbolo, contador creciente

def escribir_triángulo_decr(tamanyo: int, simbolo: str) -> None:
    for fila in range(0, tamanyo):
        print(simbolo * (tamanyo - fila))

escribir_triángulo_decr(3, 'a')
escribir_triángulo_decr(5, '#')
escribir_triángulo_decr(6, '*')

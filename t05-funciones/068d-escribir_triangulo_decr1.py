# Crea una función "escribir_triángulo_decr", que reciba un 
# tamaño y un símbolo, y escriba un triángulo alineado a la 
# izquierda decreciente, algo como:

# ****
# ***
# **
# *

# Versión decreciente 1: multiplicando el símbolo

def escribir_triángulo_decr(tamanyo: int, simbolo: str) -> None:
    for fila in range(tamanyo,0,-1):
        print(simbolo * fila)

escribir_triángulo_decr(3, 'a')
escribir_triángulo_decr(5, '#')
escribir_triángulo_decr(6, '*')

# Crea una función "escribir_triángulo_decr", que reciba un 
# tamaño y un símbolo, y escriba un triángulo alineado a la 
# izquierda decreciente, algo como:

# ****
# ***
# **
# *

# Versión decreciente 3: contador adicional

def escribir_triángulo_decr(tamanyo: int, simbolo: str) -> None:
    cantidad = tamanyo
    for fila in range(0, tamanyo):
        print(simbolo * cantidad)
        cantidad -= 1

escribir_triángulo_decr(3, 'a')
escribir_triángulo_decr(5, '#')
escribir_triángulo_decr(6, '*')

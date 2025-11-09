# Crea una función "escribir_triángulo_crec", que reciba un tamaño y un símbolo, 
# y escriba un triángulo creciente alineado a la izquierda, algo como:

# *
# **
# ***
# ****

# Versión 1: multiplicando el símbolo. La fila comienza en 1.

def escribir_triangulo_crec(tamanyo: int, simbolo: str) -> None:
    for fila in range(1,tamanyo+1):
        print(simbolo * fila)

escribir_triangulo_crec(3, 'a')
escribir_triangulo_crec(5, '#')
escribir_triangulo_crec(6, '*')

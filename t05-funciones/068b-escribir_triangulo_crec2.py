# Crea una función "escribir_triángulo_crec", que reciba un tamaño y un símbolo, 
# y escriba un triángulo creciente alineado a la izquierda, algo como:

# *
# **
# ***
# ****

# Versión 2: multiplicando el símbolo. La fila comienza en 0.

def escribir_triángulo_crec(tamanyo: int, simbolo: str) -> None:
    for fila in range(tamanyo):
        print(simbolo * (fila+1))

escribir_triángulo_crec(3, 'a')
escribir_triángulo_crec(5, '#')
escribir_triángulo_crec(6, '*')

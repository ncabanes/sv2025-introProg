# Crea una función "escribir_triángulo_crec", que reciba un tamaño y un símbolo, 
# y escriba un triángulo creciente alineado a la izquierda, algo como:

# *
# **
# ***
# ****

# Versión 3: bucle anidado

def escribir_triángulo_crec(tamanyo: int, simbolo: str) -> None:
    for fila in range(1,tamanyo+1):
        for columna in range(1,fila+1):
            print(simbolo, end="")
        print()

escribir_triángulo_crec(3, 'a')
escribir_triángulo_crec(5, '#')
escribir_triángulo_crec(6, '*')

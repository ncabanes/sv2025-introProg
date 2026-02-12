# Función "segundo_mayor(lista)": si la lista es [1, 2, 3, 5, 4], 
# el segundo dato mayor es 4.

# Versión 1: primero hallamos el máximo 
# y luego damos una segunda pasada

def segundo_mayor(lista):

    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero

    segundo = -1000000 # Valor inicial "claramente falso"
    for numero in lista:
        if numero > segundo and numero < maximo:
            segundo = numero

    return segundo


print(segundo_mayor([1, 2, 3, 5, 4]))

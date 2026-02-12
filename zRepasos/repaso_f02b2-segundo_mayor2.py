# Función "segundo_mayor(lista)": si la lista es [1, 2, 3, 5, 4], 
# el segundo dato mayor es 4.

# Versión 2: ordenamos y extraemos el penúltimo 
# Problema: cambia el orden de la lista, si es una variable

def segundo_mayor(lista: list) -> int:
    lista.sort()
    return lista[-2]

print(segundo_mayor([1, 2, 3, 5, 4]))

print()
segunda_lista = [3, 2, 1]
print(segunda_lista)
print(segundo_mayor(segunda_lista))
print(segunda_lista)

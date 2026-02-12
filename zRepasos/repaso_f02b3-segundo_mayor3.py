# Función "segundo_mayor(lista)": si la lista es [1, 2, 3, 5, 4], 
# el segundo dato mayor es 4.

# Versión 3: a partir de una copia ordenada de la lista
# (no lo hemos estudiado)
# Si hay datos duplicados, antes se debería volcar a un conjunto 
# para eliminarlo: sorted(set(lista))[2]

def segundo_mayor(lista: list) -> int:
    return sorted(lista)[-2]

lista = [1, 2, 3, 5, 4]
print(lista)
print(segundo_mayor(lista))
print(lista)

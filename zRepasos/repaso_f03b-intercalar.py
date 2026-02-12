# Función "intercalar(lista1, lista2)": devolverá el resultado 
# de fusionar ambas listas, ordenado. Por ejemplo, si lista1 
# es [1, 2, 3, 3, 4]y lista2 es [2, 6, 4, 5], el resultado 
# sería [1, 2, 3, 4, 5, 6].

def intercalar(l1: list, l2: list) -> list:
    conjunto_union = set(l1) | set(l2)
    return list(conjunto_union)

lista1 = [1, 2, 3, 3, 4]
lista2 = [2, 6, 4, 5]
print(intercalar(lista1, lista2))

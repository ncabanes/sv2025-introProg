# Crea una función posicion(cadena,letra), que devuelva la posición 
# en la que una cierta letra se encuentra dentro de una cadena, 
# contando desde 0 (o -1, si no aparece).

# Versión 1, la más natural (con 2 "return")

def posicion(texto:str, letra_buscar:str) -> int:
    for i in range(len(texto)):
        if texto[i] == letra_buscar:
            return i
    return -1

print(posicion("hola","o"))
print(posicion("hola","x"))

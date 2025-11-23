# Crea una función posicion(cadena,letra), que devuelva la posición 
# en la que una cierta letra se encuentra dentro de una cadena, 
# contando desde 0 (o -1, si no aparece).

# Versión 4, empleando "str.find" (que también permite subcadenas
# de longitud mayor que uno).

def posicion(texto:str, letra_buscar:str) -> int:
    return texto.find(letra_buscar)

print(posicion("hola","o"))
print(posicion("hola","x"))

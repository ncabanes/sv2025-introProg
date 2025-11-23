# Crea una función posicion(cadena,letra), que devuelva la posición 
# en la que una cierta letra se encuentra dentro de una cadena, 
# contando desde 0 (o -1, si no aparece).

# Versión 2, menos deseable: un único "return", pero a cambio
# necesita interrumpir el bucle para no devolver la última posición
# Usa "break", desaconsejado

def posicion(texto:str, letra_buscar:str) -> int:
    posicion = -1
    for i in range(len(texto)):
        if texto[i] == letra_buscar:
            posicion = i
            break
    return posicion

print(posicion("hola","o"))
print(posicion("hola","x"))

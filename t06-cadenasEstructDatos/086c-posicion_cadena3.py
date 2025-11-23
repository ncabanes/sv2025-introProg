# Crea una función posicion(cadena,letra), que devuelva la posición 
# en la que una cierta letra se encuentra dentro de una cadena, 
# contando desde 0 (o -1, si no aparece).

# Versión 3, usa un "while" para evitar "break"
# Más previsible que la versión con "for"+"break", pero más larga

def posicion(texto:str, letra_buscar:str) -> int:
    posicion = -1
    encontrado = False
    i = 0
    while i < len(texto) and not encontrado:
        if texto[i] == letra_buscar:
            posicion = i
            encontrado = True
        i += 1
    return posicion

print(posicion("hola","o"))
print(posicion("hola","x"))

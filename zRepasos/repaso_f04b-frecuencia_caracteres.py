# Función "frecuencia_caracteres(texto)": devolverá un diccionario 
# con cada letra y la cantidad de veces que aparece. Por ejemplo, 
# si el texto es devolverá "ahora", debería devolver 
# {"a": 2, "h": 1, "o": 1, "r": 1}


def frecuencia_caracteres(texto: str) -> dict:
    diccionario = { }
    for letra in texto:
        if not letra in diccionario:
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1
    return diccionario

print(frecuencia_caracteres("ahora"))

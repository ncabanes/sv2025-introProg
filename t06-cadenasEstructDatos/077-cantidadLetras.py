# Crea una función "cantidad(texto, letra)", que devuelva la 
# cantidad de veces que aparece una letra en un cierto texto.

def cantidad(texto, letra):
    veces = 0
    for l in texto:
        if l == letra:
            veces += 1
    return veces

print(cantidad("Hasta mañana", "a"))

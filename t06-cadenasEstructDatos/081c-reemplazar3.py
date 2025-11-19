# Crea una función "reemplazar(cadena, letraIni, letraFin)", que 
# devuelva el resultado de reemplazar una letra por otra en una 
# cadena, empleando un "for".

# Versión 3, extrayendo letras

def reemplazar(texto: str, letraIni: str, letraFin: str) -> str:
    respuesta = ""
    for letra in texto:
        if letra == letraIni:
            respuesta += letraFin
        else:
            respuesta += letra
    return respuesta

    # return texto.replace(letraIni, letraFin)

print(reemplazar("Hola","o","a"))

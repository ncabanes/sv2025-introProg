# Crea una función "reemplazar(cadena, letraIni, letraFin)", que 
# devuelva el resultado de reemplazar una letra por otra en una 
# cadena, empleando un "for".

# Versión 2, recorriendo números de posición

def reemplazar(texto: str, letraIni: str, letraFin: str) -> str:
    respuesta = ""
    for i in range(len(texto)):
        if texto[i] == letraIni:
            respuesta += letraFin
        else:
            respuesta += texto[i]
    return respuesta

print(reemplazar("Hola","o","a"))

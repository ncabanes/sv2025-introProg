# Crea una función "reemplazar(cadena, letraIni, letraFin)", que 
# devuelva el resultado de reemplazar una letra por otra en una 
# cadena, empleando un "for".

# Versión 1, que no funciona (no se puede modificar así una cadena)

def reemplazar(texto: str, letraIni: str, letraFin: str) -> str:
    for i in range(len(texto)):
        if texto[i] == letraIni:
            texto[i] = letraFin
    return texto

print(reemplazar("Hola","o","a"))

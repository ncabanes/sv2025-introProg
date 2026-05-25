# Repaso para junio 68

# 68.- Crea una función "extraerVocales", que devuelva una cadena 
# formada por las vocales (en minúsculas, desprecia los acentos) que 
# contenga el texto que se indique como parámetro. Pruébala. Por ejemplo, 
# si pides extraer las vocales de "Adiós", debería devolverte "ai".

# Versión 2: sin repetir vocales en la respuesta

def extraerVocales(texto: str) -> str:
    respuesta = ""
    for letra in texto.lower():
        if letra in "aeiou":
            if not letra in respuesta:
                respuesta += letra
    return respuesta
    
def extraerVocales2(texto: str) -> str:
    respuesta = ""
    if "a" in texto.lower():
        respuesta += "a"
    if "e" in texto.lower():
        respuesta += "e"
    if "i" in texto.lower():
        respuesta += "i"
    if "o" in texto.lower():
        respuesta += "o"
    if "u" in texto.lower():
        respuesta += "u"
    return respuesta

def extraerVocales3(texto: str) -> str:
    respuesta = ""
    for vocal in "aeiou":
        if vocal in texto.lower():
            respuesta += vocal
    return respuesta


print(extraerVocales("Adiós")) # Escribiría: ai
print(extraerVocales("Hasta mañana")) # Escribiría: a

print(extraerVocales2("Adiós")) # Escribiría: ai
print(extraerVocales2("Hasta mañana")) # Escribiría: a

print(extraerVocales3("Adiós")) # Escribiría: ai
print(extraerVocales3("Hasta mañana")) # Escribiría: a

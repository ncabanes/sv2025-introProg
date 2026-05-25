# Repaso para junio 68

# 68.- Crea una función "extraerVocales", que devuelva una cadena 
# formada por las vocales (en minúsculas, desprecia los acentos) que 
# contenga el texto que se indique como parámetro. Pruébala. Por ejemplo, 
# si pides extraer las vocales de "Adiós", debería devolverte "ai".

# Versión 1: si una vocal esta repetida, se devuelve repetida

def extraerVocales(texto: str) -> str:
    respuesta = ""
    for letra in texto.lower():
        if letra in "aeiou":
            respuesta += letra
    return respuesta
    

print(extraerVocales("Adiós")) # Escribiría: ai
print(extraerVocales("Hasta mañana")) # Escribiría: aaaaa

"""
2. Crea una función "contar_vocales", que devolverá la cantidad de 
vocales (en mayúsculas o minúsculas) que contiene el texto que se 
indica como parámetro (no te preocupes por las vocales acentuadas). Por 
ejemplo, si el texto es "Ahora", debería devolver 3. Pruébala desde el 
cuerpo del programa.
"""

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra in "AEIOUaeiou":
            contador += 1
    return contador

print('Vocales en "Ahora": ', contar_vocales("Ahora"))

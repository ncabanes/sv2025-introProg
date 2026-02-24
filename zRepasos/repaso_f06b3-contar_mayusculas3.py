"""
2. Crea una función "contar_mayusculas", que devolverá la cantidad 
de letras en mayúsculas (del alfabeto inglés) que contiene el texto
que se indica como parámetro. Por ejemplo, si el texto es "Ahora",
debería devolver 1. Pruébala desde el cuerpo del programa.
"""

# Versión 3: ver si aparece en una lista de letras

def contar_mayusculas(texto: str) -> int:
    contador = 0
    for letra in texto:
        if letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            contador += 1
    return contador

print(contar_mayusculas("Ahora"))

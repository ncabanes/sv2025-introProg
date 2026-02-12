# Función "contar_palabra_en_frase(palabra, frase)": 
# si la palabra es "hola" y la frase es 
# "Hola hola aholados aholados", debería devolver 2.

# Forma exhaustiva (la esperable)

def contar_palabra_en_frase(palabra, frase):
    palabra = palabra.lower()
    palabras_frase = frase.lower().split()
    cantidad = 0
    for p in palabras_frase:
        if p == palabra:
            cantidad += 1
    return cantidad

print(contar_palabra_en_frase("hola", "Hola hola aholados aholados"))

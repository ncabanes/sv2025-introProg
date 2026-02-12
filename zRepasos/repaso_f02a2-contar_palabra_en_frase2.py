# Función "contar_palabra_en_frase(palabra, frase)": 
# si la palabra es "hola" y la frase es 
# "Hola hola aholados aholados", debería devolver 2.

# Forma abreviada (no esperable: no hemos usado "count" en listas)

def contar_palabra_en_frase(palabra: str, frase: str) -> int:
    return frase.upper().split().count(palabra.upper())
    
print(contar_palabra_en_frase("hola", "Hola hola alohalo hlosj"))

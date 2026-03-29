# Repaso para junio 34

# Crea una función "cantidad_de_vocales(texto)", que reciba como 
# parámetro un texto y devuelva la cantidad de vocales que contiene ese 
# texto. Por ejemplo, para el texto "Hola", debería devolver 2. Pruébala 
# desde el cuerpo del programa.

# --- Función -----
def cantidad_de_vocales(texto: str) -> int:
    cantidad = 0
    for letra in texto:
        if letra in "AEIOUaeiou":
            cantidad += 1
    return cantidad

# --- Cuerpo del programa -----
print(cantidad_de_vocales("Hola"))
print(cantidad_de_vocales("Hasta mañana"))
print(cantidad_de_vocales("Ahora ya me sale!!!"))

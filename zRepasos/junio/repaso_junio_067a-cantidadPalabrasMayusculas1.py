# Repaso para junio 67

# 67.- Crea una función llamada "cantidadPalabrasMayusculas", que 
# reciba como parámetro una lista de palabras y devuelva la cantidad de 
# ellas que están en mayúsculas. Por ejemplo, si las palabras son "Hola", 
# "AJAX" y "adeu", debería devolver el valor 1. Pruébala en un programa 
# que pida 4 palabras al usuario y le responda cuantas de esas 4 están en 
# mayúsculas.

# Versión 1, todavía sin función

lista = ["Hola", "AJAX", "adeu"]

cantidad = 0
for palabra in lista:
    if palabra == palabra.upper():
        cantidad += 1

print(cantidad)

# Pedir al usuario 10 palabras y guardarlas en una lista.
# Preguntar de forma repetitiva qué texto quiere buscar.
# Responder si está entre los 10 iniciales. 
# Deja de repetir cuando se introduzca “fin”.

palabras = []
for i in range(10):
    palabra = input("Dime una palabra: ")
    palabras.append(palabra)
    
buscar = input("Palabra a buscar? ")
while buscar != "fin":
    if buscar in palabras:
        print("Estaba")
    else:
        print("No estaba")
    buscar = input("Palabra a buscar? ")

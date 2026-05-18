# Repaso para junio 62

# 62.- Pide al usuario que introduzca una palabra y luego otra palabra de 
# la misma longitud. Después de leer ambas, responde "Perfecto" o "Algo 
# falla", según corresponda. Por ejemplo, si introduce "hola" y "ciao", 
# tu respuesta debería ser "Perfecto"; si introduce "hola" y "adios", 
# deberías responder "Algo falla".

palabra1 = input("Dime la primera palabra: ")
palabra2 = input("Dime la segunda palabra, de la misma longitud: ")

if len(palabra1) == len(palabra2):
    print("Perfecto")
else:
    print("Algo falla")

# Crea una función "es_par", que devuelva True o False según si el número 
# entero que se le indica como parámetro es par o no lo es.

# Versión 2: devolviendo el resultado de evaluar la condición

def es_par(n : int) -> bool:
    return n % 2 == 0

print( es_par(12) )

if es_par(15):
    print("15 es par")
else:
    print("15 no es par")
    

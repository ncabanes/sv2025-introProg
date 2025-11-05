# Crea una función "es_par", que devuelva True o False según si el número 
# entero que se le indica como parámetro es par o no lo es.

# Versión 1: con "if"

def es_par(n : int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


print( es_par(12) )

if es_par(15):
    print("15 es par")
else:
    print("15 no es par")
    

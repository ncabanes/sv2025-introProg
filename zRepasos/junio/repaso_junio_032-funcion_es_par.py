# Repaso para junio 32

# Crea una función "es_par(n)", que reciba como parámetro 
# un número entero y devuelva el dato booleano "verdadero" 
# (True) o "falso" (False) según corresponda. Pruébala desde 
# el cuerpo del programa.

# --- Función -----
def es_par(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

# --- Cuerpo del programa -----
if (es_par(5)):
    print("5 es par")
else:
    print("5 es impar")

if (es_par(10)):
    print("10 es par")
else:
    print("10 es impar")

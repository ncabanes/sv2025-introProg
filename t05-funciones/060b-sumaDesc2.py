# Función suma_desc (suma descendente desde el primer número que
# se indique como parámetro, o hasta 1, si no se indica segundo
# parámetro)

# Versión 2: con "type hinting"

def suma_desc(n1 : int, n2 : int = 1) -> int:
    suma : int = 0
    for i in range(n1, n2-1, -1):
        suma += i
    return suma

print(suma_desc(7,5))
print(suma_desc(3))

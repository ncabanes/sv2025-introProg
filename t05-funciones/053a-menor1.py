# Función menor (devuelve el menor de los 
# dos números que se indiquen como parámetros)

# Versión 1: sin type hinting

def menor(n1, n2):
    if n1 < n2:
        return n1
    else:
        return n2


x = menor(5, 7)
print(x)
y = menor(15, 10)
print(y)
print( menor(-8, -8) )

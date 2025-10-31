# Crea una función "mayor_de_3", que reciba como parámetros tres números reales 
# y devuelva el valor numérico del mayor de ellos.

# Versión 1: sin "type hinting"

def mayor_de_3(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

x = mayor_de_3( 7, 10, -1.5 )
print(x)

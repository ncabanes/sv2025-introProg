# Crea una función "mayor_digito", que a partir de un 
# número como el 12354 devolverá el número 5 (la mayor
# de las cifras que forman ese número entero).

def mayor_digito(n: int) -> int:
    cadena = str(n)
    mayor = cadena[0]
    for cifra in cadena:
        if cifra > mayor:
            mayor = cifra
    return int(mayor)
    
print(mayor_digito(12354))

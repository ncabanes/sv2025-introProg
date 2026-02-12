# Crea una función "mayor_digito", que a partir de un 
# número como el 12354 devolverá el número 5 (la mayor
# de las cifras que forman ese número entero).

def mayor_digito(n):
    mayor = 0

    while n > 0:
        digito = n % 10       # Extraemos el último dígito
        if digito > mayor:
            mayor = digito
        n //= 10              # Eliminamos el último dígito

    return mayor

print(mayor_digito(12354))

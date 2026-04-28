# Repaso para junio 54

# (Ejemplo de examen de mínimos, 6/12)

# 54.- Crea una función llamada "cubo", que devuelva el resultado de 
# elevar al cubo el número real que reciba como parámetro. Pruébala.

# Versión 1: sin indicar tipos de datos


# Previo: las dos formas de elevar un número al cubo

print(2 * 2 * 2)
print(2 ** 3)


# Ahora sí: la función y su prueba

def cubo(n):
    return n * n * n

print(cubo(2))

# Crea una función "potencia(base, exponente)", que devuelva el resultado 
# de elevar "base" a "exponente", sin utilizar **, sino con un bucle "for".

def potencia(base: int, exponente: int) -> int:
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

print(potencia(5,3))
print(5**3)

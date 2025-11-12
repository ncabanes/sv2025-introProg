# Mínimo común múltiplo, probando todos los valores

def mcm(a: int, b: int) -> int:

    # Hallo el mayor
    if a > b:
        mayor = a
    else:
        mayor = b

    # Busco múltiplos desde a*b hasta el mayor
    multiploProvisional = a*b
    for i in range(a*b, mayor-1, -1):
        if i % a == 0 and i % b == 0:
            multiploProvisional = i
            
    # El menor que haya encontrado es mi solución
    return multiploProvisional

print("mcm(20,15) =",mcm(20,15))
print("mcm(1,10) =",mcm(1,10))
print("mcm(2,4) =",mcm(2,4))





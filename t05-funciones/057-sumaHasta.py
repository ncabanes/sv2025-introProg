# Función suma_hasta (suma de los números desde 1 hasta el que 
# se indique como parámetro)

def suma_hasta(n : int) -> int:
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

print(suma_hasta(5))

x = suma_hasta(10)
print(x)

suma_hasta(20)

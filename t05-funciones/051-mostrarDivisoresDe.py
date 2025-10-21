# Función mostrarDivisoresDe 

# Muestra los divisores de un número, separados
# por un espacio en blanco y luego salta de línea

def mostrarDivisoresDe(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")
    print()


mostrarDivisoresDe(8)
mostrarDivisoresDe(15)
mostrarDivisoresDe(123456)

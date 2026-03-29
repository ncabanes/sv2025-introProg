# Repaso para junio 33

# Crea una función "escribir_pares_entre(n1, n2)", que reciba 
# como parámetros dos números enteros, muestre en pantalla la 
# lista de números pares que hay entre el primero y el segundo, 
# ambos incluidos, en la misma línea, separados por espacios 
# en blanco. Por ejemplo, si los números son 3 y 8, debería 
# escribir "4 6 8 ".

# La función que se nos pedía
def escribir_pares_entre(n1: int, n2: int) -> None:
    for i in range(n1, n2+1):
        if i % 2 == 0:
            print(i, end=" ")

# Cuerpo del programa
escribir_pares_entre(3, 8)
# Debería aparecer: 4 6 8 

print()
escribir_pares_entre(10,19)

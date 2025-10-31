# Crea una función "mostrarParesEntre", que reciba como parámetros dos números 
# enteros y escriba, en una misma línea, todos los números pares que hay entre 
# ellos.

def mostrarParesEntre(n1, n2):
    for i in range(n1, n2+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

mostrarParesEntre(5,20)
mostrarParesEntre(15,41)

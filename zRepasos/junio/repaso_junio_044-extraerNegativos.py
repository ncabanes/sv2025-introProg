# 44.- Crea una función "extraer_negativos", que recibirá como 
# parámetro una lista de números y devolverá una nueva lista formada por 
# los números negativos que contenga esa lista inicial. Crea una segunda 
# función "mostrar_lista", que mostrará el contenido de una lista de 
# números en pantalla, todos ellos en la misma línea, separados por un 
# espacio en blanco. Usa ambas funciones para crear una nueva versión del 
# ejercicio anterior.

def extraer_negativos(numeros: list) -> list:
    resultados = []
    for n in numeros:
        if n < 0 :
            resultados.append(n)
    return resultados

def mostrar_lista(lista: list) -> None:
    for n in lista:
        print(n, end=" ")


# ----- Cuerpo del programa -------

numeros = [ ]

n = int(input("Dime un número: "))
while n != 0:
    numeros.append(n)
    n = int(input("Dime un número: "))

negativos = extraer_negativos(numeros)
mostrar_lista(negativos)

if len(negativos) == 0:
    print("No había negativos")

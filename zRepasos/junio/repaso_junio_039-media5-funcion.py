# Repaso para junio 39

# 39.- Crea una función "media_de_lista", 
# que reciba como parámetro una lista de 
# números y devuelva su media. Por ejemplo, 
# si la lista es [3.5, 6.5, 8], debería 
# devolver el valor 6 (que es la media 
# aritmética de 3.5, 6.5 y 8). Pruébala 
# desde el cuerpo del programa, haciendo 
# una nueva versión del ejercicio anterior.

def media_de_lista(lista: list) -> float:
    suma = 0
    for dato in lista:
        suma += dato
    return suma/len(lista)

# Pedir datos
lista = [ ]
n = float(input("Dime un número: "))
while n != 0 :
    lista.append(n)
    n = float(input("Dime un número: "))

# Calcular resultados
print("La media es", media_de_lista(lista))

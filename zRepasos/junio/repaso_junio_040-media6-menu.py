# 40 Vamos a crear un programa de estadística 
# sencillo. Mostrará un menú que permita al 
# usuario: añadir un nuevo dato, mostrar todos 
# los datos, calcular y mostrar la media, salir.

def anyadir(lista : list)-> list:
    dato = float(input("Dato a añadir: "))
    lista.append(dato)
    return lista

def mostrar_datos(lista : list)-> None:
    for dato in lista:
        print(dato, end=" ")
    print()
    
def media_de_lista(lista: list) -> float:
    suma = 0
    for dato in lista:
        suma += dato
    return suma/len(lista)

def mostrar_media(lista: list)-> None:
    if len(lista) == 0:
        print("No hay datos.")
    else:
        print("La media de los datos de la lista es: ", 
            media_de_lista(lista))

lista = []
terminado = False

while not terminado:
    print("-----MENU-----")
    print("1. Añadir")
    print("2. Mostrar Datos")
    print("3. Ver media")
    print("4. Salir")

    opc = int(input("Elige una opcion: "))

    if opc == 1:
        lista = anyadir(lista)
    elif opc == 2:
        mostrar_datos(lista)
    elif opc == 3:
        mostrar_media(lista)
    elif opc == 4:
        terminado = True
    else:
        print("Opción no valida.")



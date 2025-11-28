lista_equipos = []
terminado = False

while not terminado:
    print("1- Añadir un equipo")
    print("2- Ver todos los equipos")
    print("S- Salir")

    opcion = input("Opción? ")
    if opcion == "1":
        detalles = input("Qué equipo? ")
        lista_equipos.append(detalles)
    if opcion == "2":
        print(lista_equipos)
    if opcion == "S":
        terminado = True

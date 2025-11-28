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
    elif opcion == "2":
        for equipo in lista_equipos:
            print(equipo)
    elif opcion.upper() == "S":
        terminado = True
    else:
        print("Opción incorrecta")

    print()

print("Hasta luego")

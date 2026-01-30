# Lista de juegos
juegos = []
terminado = False
while not terminado:

    print("1- Añadir un nuevo juego")
    print("2- Editar un juego")
    print("3- Ver todos los juegos")
    print("4- Ordenar los juegos")
    print("0- Salir")

    opcion = input("Qué opcion? ")
    print()

    if opcion == "1":
        print("Añadir")
        juego = input("Dime el juego: ")
        genero = input("Dime el género: ")
        plataforma = input("Dime la plataforma: ")
        juegos.append( { "nombre" : juego,
            "genero" : genero,
            "plataforma" : plataforma })

    elif opcion == "2":
        print("Editar")
        num_juego = int(input("Número de juego a modificar: "))
        nuevo_texto = input("Nuevo nombre del juego: ")
        nuevo_genero = input("Dime el género: ")
        nueva_plataforma = input("Dime la plataforma: ")

        juegos[ num_juego-1 ] = { "nombre" : nuevo_texto,
            "genero" : nuevo_genero,
            "plataforma" : nueva_plataforma }

    elif opcion == "3":
        print("Ver")
        for i in range(len(juegos)):
            print(i+1, juegos[i]["nombre"],
                "-",juegos[i]["genero"],
                " (",juegos[i]["plataforma"], ")")

    elif opcion == "4":
        print("Esta versión aún no puede ordenar")
        #juegos.sort()

    elif opcion == "0":
        terminado = True
        print("Hasta luego")

    else:
        print("Opción no válida")

print("Hasta otra!")

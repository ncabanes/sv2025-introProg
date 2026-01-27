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
        juegos.append(juego)

    elif opcion == "2":
        print("Editar")
        num_juego = int(input("Número de juego a modificar: "))
        nuevo_texto = input("Nuevo nombre del juego: ")
        juegos[ num_juego-1 ] = nuevo_texto

    elif opcion == "3":
        print("Ver")
        for i in range(len(juegos)):
            print(i+1, juegos[i])

    elif opcion == "4":
        print("Ordenar")
        juegos.sort()

    elif opcion == "0":
        terminado = True
        print("Hasta luego")

    else:
        print("Opción no válida")

print("Hasta otra!")

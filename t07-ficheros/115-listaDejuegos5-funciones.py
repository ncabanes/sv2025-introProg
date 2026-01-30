def cargar() -> list:
    juegos = []

    fichero = open("juegos.txt", "r")
    linea = fichero.readline().rstrip()
    while linea:
        fragmentos = linea.split("#")
        
        juego = fragmentos[0]
        genero = fragmentos[1]
        plataforma = fragmentos[2]
        
        juegos.append( { "nombre" : juego,
            "genero" : genero,
            "plataforma" : plataforma })

        linea = fichero.readline().rstrip()
    fichero.close()
    
    return juegos


def guardar(datosJuegos: list) -> None:
    fichero = open("juegos.txt", "w")
    for i in range(len(datosJuegos)):
        fichero.write(datosJuegos[i]["nombre"] + "#")
        fichero.write(datosJuegos[i]["genero"] + "#")
        fichero.write(datosJuegos[i]["plataforma"] + "\n")
    fichero.close()


def ver(juegos: list) -> None:
    print("Ver")
    for i in range(len(juegos)):
        print(i+1, juegos[i]["nombre"],
            "-",juegos[i]["genero"],
            " (",juegos[i]["plataforma"], ")")


def anadir(juegos: list) -> list:
    print("Añadir")
    juego = input("Dime el juego: ")
    genero = input("Dime el género: ")
    plataforma = input("Dime la plataforma: ")
    juegos.append( { "nombre" : juego,
        "genero" : genero,
        "plataforma" : plataforma })
    
    return juegos


def modificar(juegos: list) -> list:
    print("Editar")
    num_juego = int(input("Número de juego a modificar: "))
    nuevo_texto = input("Nuevo nombre del juego: ")
    nuevo_genero = input("Dime el género: ")
    nueva_plataforma = input("Dime la plataforma: ")

    juegos[ num_juego-1 ] = { "nombre" : nuevo_texto,
        "genero" : nuevo_genero,
        "plataforma" : nueva_plataforma }

    return juegos


def mostrar_menu() -> None:
    print()    
    print("1- Añadir un nuevo juego")
    print("2- Editar un juego")
    print("3- Ver todos los juegos")
    print("4- Ordenar los juegos")
    print("0- Salir")


# Lista de juegos - cuerpo del programa
juegos = cargar()
terminado = False
while not terminado:
    mostrar_menu()
    opcion = input("Qué opcion? ")
    if opcion == "1":
        juegos = anadir(juegos)
    elif opcion == "2":
        juegos = modificar(juegos)
    elif opcion == "3":
        ver(juegos)
    elif opcion == "4":
        print("Esta versión aún no puede ordenar")
        #juegos.sort()
    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

guardar(juegos)

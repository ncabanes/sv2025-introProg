# 48.- Crea una versión todavía más modular del ejercicio anterior: la 
# opción de mostrar todas las películas estará dentro de la función 
# "mostrar_todo(lista)", que recibirá la lista actual como parámetro, 
# mostrará cada una de las películas en una línea y no devolverá ningún 
# resultado; la opción de "buscar" recibirá la lista actual como 
# parámetro, preguntará al usuario el nombre de la película a buscar, le 
# responderá si está o no, y no devolverá ningún resultado; la opción de 
# "añadir una película" estará dentro de la función 
# "anyadir_pelicula(lista)", que recibirá la lista actual como parámetro, 
# pedirá al usuario una nueva película, la añadirá al final de la lista y 
# devolverá la lista modificada.

def cargar_peliculas() -> list:
    peliculas = [ ]
    try:
        fichero = open("peliculas.txt", "r")
        for linea in fichero:
            peliculas.append(linea.rstrip())
        fichero.close()
    except:
        print("No había datos")
    
    return peliculas
    

def guardar_peliculas(peliculas: list) -> None:
    fichero = open("peliculas.txt", "w")
    for p in peliculas:
        fichero.write(p + "\n")
    fichero.close()

def mostrar_todo(peliculas: list) -> None:
    for p in peliculas:
        print(p)

def anyadir_pelicula(peliculas: list) -> list:
    titulo = input("Qué nueva película añadimos? ")
    peliculas.append(titulo)
    return peliculas

def buscar(peliculas: list) -> None:
    titulo = input("Qué titulo buscamos? ")
    encontrado = False
    for p in peliculas:
        if titulo.upper() in p.upper():
            encontrado = True

    if encontrado:
        print("Existe!")
    else:
        print("No existe!")


# ----------- Cuerpo del programa

peliculas = cargar_peliculas()
terminado = False
while not terminado:
    print("1- Buscar película")
    print("2- Mostrar todas")
    print("3- Añadir otra película")
    print("S- Salir")
    opcion = input("Opción: ").upper()
    
    if opcion == "S":
        terminado = True
    elif opcion == "1":
        buscar(peliculas)
    elif opcion == "2":
        mostrar_todo(peliculas)
    elif opcion == "3":
        peliculas = anyadir_pelicula(peliculas)

guardar_peliculas(peliculas)

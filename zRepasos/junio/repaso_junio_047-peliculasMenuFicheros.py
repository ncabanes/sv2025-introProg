# 47.- Crea una función "cargar_peliculas", que lea el contenido del 
# fichero "peliculas.txt" y lo vuelque a una lista, que devolverá como 
# resultado. Crea una otra función "guardar_peliculas(lista)", que reciba 
# como parámetro una lista de películas y las guarde en el fichero 
# "peliculas.txt", sin devolver nada. Usa ambas funciones para crear una 
# versión mejorada del ejercicio anterior.

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

    elif opcion == "1": # Buscar
        titulo = input("Qué titulo buscamos? ")
        encontrado = False
        for p in peliculas:
            if p == titulo:
                encontrado = True

        if encontrado:
            print("Existe!")
        else:
            print("No existe!")

    elif opcion == "2": # Ver todas
        for p in peliculas:
            print(p)

    elif opcion == "3": # Añadir
        titulo = input("Qué nueva película añadimos? ")
        peliculas.append(titulo)

guardar_peliculas(peliculas)

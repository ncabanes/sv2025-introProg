# 46.- Crea una versión mejorada del programa anterior: Mostrará un 
# menú que permita comprobar si una película aparece en nuestra lista, 
# mostrar todas ellas, añadir una nueva o salir. Al terminar la 
# ejecución, los datos se guardarán en el fichero "peliculas.txt", y se 
# cargarán desde ese fichero (si existe) al principio del programa

peliculas = [ ]
fichero = open("peliculas.txt", "r")
for linea in fichero:
    peliculas.append(linea.rstrip())
fichero.close()

terminado = False
while not terminado:
    print("1- Buscar película")
    print("2- Mostrar todas")
    print("3- Añadir otra película")
    print("S- Salir")
    opcion = input("Opción").upper()
    
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


fichero = open("peliculas.txt", "w")
for p in peliculas:
    fichero.write(p + "\n")
fichero.close()

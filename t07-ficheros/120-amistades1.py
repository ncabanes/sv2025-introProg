# Debes crear una pequeña base de datos en la que poder anotar tus 
# amigos. De cada uno de ellos, queremos su nombre, email y año de 
# nacimiento. Debe permitir añadir un nuevo amigo, ver todos ellos, 
# modificar uno o buscar los que contengan un cierto texto. Los datos se 
# guardarán cuando termine la ejecución y se cargarán (si existen) en la 
# ejecución siguiente.

# Versión 1: sin ficheros ni funciones

amistades = []
terminado = False
while not terminado:

    print("1- Añadir un nuevo amigo")
    print("2- Ver todos los amigos")
    print("3- Modificar un amigo")
    print("4- Buscar un amigo")
    print("0- Salir")

    opcion = input("Qué opcion? ")
    print()

    if opcion == "1":
        print("Añadir")
        nombre = input("Dime el nombre: ")
        email = input("Dime el e-mail: ")
        anyo = int(input("Dime el año de nacimiento: "))
        amistades.append( { "nombre" : nombre,
            "email" : email,
            "año" : anyo })
 
    elif opcion == "2":
        print("Ver")
        for i in range(len(amistades)):
            print(i+1, amistades[i]["nombre"],
                "-",amistades[i]["email"],
                "-",amistades[i]["año"])

    elif opcion == "3":
        print("Modificar")
        num_amigo = int(input("Número de amigo a modificar: "))
        nuevo_nombre = input("Nuevo nombre del amigo: ")
        nuevo_email = input("Nuevo e-mail: ")
        nuevo_anyo = int(input("Nuevo año: "))

        amistades[ num_amigo-1 ] = { "nombre" : nuevo_nombre,
            "email" : nuevo_email,
            "año" : nuevo_anyo }

    elif opcion == "4":
        print("Buscar")
        busqueda = input("Nombre (o fragmento) a buscar: ")
        for i in range(len(amistades)):
            if busqueda.lower() in amistades[i]["nombre"].lower():
                print(i+1, amistades[i]["nombre"],
                    "-",amistades[i]["email"],
                    "-",amistades[i]["año"])

    elif opcion == "0":
        terminado = True

    else:
        print("Opción no válida")

print("Hasta otra!")

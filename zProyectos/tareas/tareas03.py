# Lista de tareas, versión 3
# Permite añadir, ver y modificar

tareas = []
terminado = False
while not terminado:

    print("1- Añadir una nueva tarea")
    print("2- Editar una tarea")
    print("3- Ver todas las tareas")
    print("0- Salir")

    opcion = input("Qué opcion? ")
    print()

    if opcion == "1":
        print("Añadir")
        tarea = input("Dime la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("Editar")
        num_tarea = int(input("Número de tarea a modificar: "))
        nuevo_texto = input("Texto para la tarea: ")
        tareas[ num_tarea-1 ] = nuevo_texto
    elif opcion == "3":
        print("Ver")
        for i in range(len(tareas)):
            print(i+1, tareas[i])
    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

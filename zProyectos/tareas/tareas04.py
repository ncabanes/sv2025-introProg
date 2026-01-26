# Lista de tareas, versión 4
# Permite añadir, ver y modificar (con prioridades)

descripc_tareas = []
prioridad_tareas = []
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
        descripc_tareas.append(tarea)
        prioridad = int(input("Dime su prioridad: "))
        prioridad_tareas.append(prioridad)
    elif opcion == "2":
        print("Editar")
        num_tarea = int(input("Número de tarea a modificar: "))
        nuevo_texto = input("Texto para la tarea: ")
        descripc_tareas[ num_tarea-1 ] = nuevo_texto
        nueva_prioridad = int(input("Prioridad para la tarea: "))
        prioridad_tareas[ num_tarea-1 ] = nueva_prioridad
    elif opcion == "3":
        print("Ver")
        for i in range(len(descripc_tareas)):
            print(i+1, descripc_tareas[i], " - ",
                prioridad_tareas[i])
    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

# Lista de tareas, versión 5, diccionarios
# Permite añadir, ver y modificar (con prioridades)

tareas = [ {
    "tarea": "estudiar",
    "prioridad": 10
},
{
    "tarea": "hacer la comida",
    "prioridad": 6
}
]

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
        prioridad = int(input("Dime su prioridad: "))
        dato_actual = {
            "tarea": tarea,
            "prioridad": prioridad
        }
        tareas.append(dato_actual)


    elif opcion == "2":
        print("Editar")
        num_tarea = int(input("Número de tarea a modificar: "))
        nuevo_texto = input("Texto para la tarea: ")
        nueva_prioridad = int(input("Prioridad para la tarea: "))

        tareas[num_tarea-1] = {
            "tarea": nuevo_texto,
            "prioridad": nueva_prioridad
        }

    elif opcion == "3":
        print("Ver")
        for i in range(len(tareas)):
            dato_actual = tareas[i]
            print(i+1, dato_actual["tarea"], " - ",
                dato_actual["prioridad"])

    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

# Lista de tareas, versión 6, diccionarios + ficheros
# Permite añadir, ver y modificar (con prioridades)

# Versión con "try-except" y manejo de ficheros con "with"

tareas = []

try:
    with open("tareas.txt", "r") as fichero:
        for linea in fichero:
            fragmentos = linea.rstrip().split("#")
        
            tarea = fragmentos[0]
            prioridad = int(fragmentos[1])

            dato_actual = {
                "tarea": tarea,
                "prioridad": prioridad
            }
            tareas.append(dato_actual)
except:
    print("Sin datos previos. Se creará un fichero nuevo.")

terminado = False
while not terminado:

    print()
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

with open("tareas.txt", "w") as fichero:
    for i in range(len(tareas)):
        fichero.write(tareas[i]["tarea"] + "#")
        fichero.write(str(tareas[i]["prioridad"]) + "\n")

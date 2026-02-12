# Lista de tareas, versión 7, diccionarios + ficheros + funciones
# Permite añadir, ver y modificar (con prioridades)

def guardar(tareas: list) -> None:
    with open("tareas.txt", "w") as fichero:
        for i in range(len(tareas)):
            fichero.write(tareas[i]["tarea"] + "#")
            fichero.write(str(tareas[i]["prioridad"]) + "\n")


def cargar() -> list:
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
    
    return tareas


def mostrar_menu() -> None:
    print()
    print("1- Añadir una nueva tarea")
    print("2- Editar una tarea")
    print("3- Ver todas las tareas")
    print("0- Salir")


def anadir(tareas: list) -> list:
    print("Añadir")
    tarea = input("Dime la tarea: ")
    prioridad = int(input("Dime su prioridad: "))
    dato_actual = {
        "tarea": tarea,
        "prioridad": prioridad
    }
    tareas.append(dato_actual)
    return tareas


def editar(tareas: list) -> list:
    print("Editar")
    num_tarea = int(input("Número de tarea a modificar: "))
    nuevo_texto = input("Texto para la tarea: ")
    nueva_prioridad = int(input("Prioridad para la tarea: "))

    tareas[num_tarea-1] = {
        "tarea": nuevo_texto,
        "prioridad": nueva_prioridad
    }
    return tareas


def ver_todas(tareas: list) -> None:
    print("Ver")
    for i in range(len(tareas)):
        dato_actual = tareas[i]
        print(i+1, dato_actual["tarea"], " - ",
            dato_actual["prioridad"])


# ---- Cuerpo del programa -----------

tareas = cargar()
terminado = False
while not terminado:
    mostrar_menu()
    opcion = input("Qué opcion? ")
    print()

    if opcion == "1":
        tareas = anadir(tareas)
    elif opcion == "2":
        tareas = editar(tareas)
    elif opcion == "3":
        ver_todas(tareas)
    elif opcion == "0":
        terminado = True
    else:
        print("Opción no válida")

guardar(tareas)
print("Hasta luego")

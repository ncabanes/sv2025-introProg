# 65. Mejora tu "menú" (ejercicio 42) para que realmente se repita 
# hasta que se escoja la opción 0.

# Versión 2b: más compacta, con booleano de control

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
    elif opcion == "2":
        print("Editar")
    elif opcion == "3":
        print("Ver")
    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

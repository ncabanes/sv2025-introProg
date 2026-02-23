import os

ARCHIVO = "clases.txt"

def cargar_datos():
    clases = []
    existe = os.path.exists(ARCHIVO)

    if existe:
        fichero = open(ARCHIVO, "r", encoding="utf-8")
        for linea in fichero:
            linea = linea.strip()
            if linea != "":
                partes = linea.split("#")
                nombre = partes[0]
                fecha = partes[1]
                hora = partes[2]
                importe = float(partes[3])
                clase = {"nombre": nombre, "fecha": fecha, "hora": hora, "importe": importe}
                clases.append(clase)
        fichero.close()

    return clases


def guardar_datos(clases):
    fichero = open(ARCHIVO, "w", encoding="utf-8")
    for clase in clases:
        linea = clase["nombre"] + "#" + clase["fecha"] + "#" + clase["hora"] + "#" + str(clase["importe"])
        fichero.write(linea + "\n")
    fichero.close()


def anadir_clase(clases):
    nombre = input("Nombre del alumno: ")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")

    clase = {"nombre": nombre, "fecha": fecha, "hora": hora, "importe": 0.0}
    clases.append(clase)

    guardar_datos(clases)
    print("Clase añadida correctamente.")

    return clases


def ver_pendientes(clases):
    print("CLASES PENDIENTES:")
    contador = 0

    for i in range(len(clases)):
        clase = clases[i]
        if clase["importe"] == 0:
            contador = contador + 1
            numero = i + 1
            print(str(numero) + ". " + clase["fecha"] + " " + clase["hora"] + " - " + clase["nombre"])

    if contador == 0:
        print("No hay clases pendientes.")


def marcar_impartida(clases):
    numero = int(input("Número de clase impartida: "))
    valido = numero >= 1 and numero <= len(clases)

    if valido:
        clase = clases[numero - 1]
        if clase["importe"] == 0:
            importe = float(input("Importe cobrado: "))
            clase["importe"] = importe
            guardar_datos(clases)
            print("Clase marcada como impartida.")
        else:
            print("Esa clase ya tenía un importe asignado.")
    else:
        print("Número incorrecto.")

    return clases


def calcular_importes(clases):
    cantidad = len(clases)
    total = 0.0

    for clase in clases:
        total = total + clase["importe"]

    if cantidad > 0:
        media = total / cantidad
    else:
        media = 0

    print("ESTADÍSTICAS:")
    print("Total de clases: " + str(cantidad))
    print("Importe total: " + str(total))
    print("Importe medio por clase: " + str(media))


def modificar_clase(clases):
    numero = int(input("Número de clase a modificar: "))
    valido = numero >= 1 and numero <= len(clases)

    if valido:
        clase = clases[numero - 1]

        nueva_fecha = input("Fecha [" + clase["fecha"] + "]: ")
        nueva_hora = input("Hora [" + clase["hora"] + "]: ")
        nuevo_nombre = input("Nombre [" + clase["nombre"] + "]: ")
        nuevo_importe = input("Importe [" + str(clase["importe"]) + "]: ")

        if nueva_fecha != "":
            clase["fecha"] = nueva_fecha
        if nueva_hora != "":
            clase["hora"] = nueva_hora
        if nuevo_nombre != "":
            clase["nombre"] = nuevo_nombre
        if nuevo_importe != "":
            clase["importe"] = float(nuevo_importe)

        guardar_datos(clases)
        print("Clase modificada correctamente.")
    else:
        print("Número incorrecto.")

    return clases


def mostrar_menu():
    print("===== GESTIÓN DE CLASES PARTICULARES =====")
    print("A - Añadir nueva clase")
    print("P - Ver clases pendientes")
    print("I - Marcar clase como impartida")
    print("T - Calcular importe total y media")
    print("M - Modificar una clase")
    print("F - Fin")


clases = cargar_datos()
continuar = True

while continuar:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    opcion = opcion.upper()

    if opcion == "A":
        clases = anadir_clase(clases)
    elif opcion == "P":
        ver_pendientes(clases)
    elif opcion == "I":
        clases = marcar_impartida(clases)
    elif opcion == "T":
        calcular_importes(clases)
    elif opcion == "M":
        clases = modificar_clase(clases)
    elif opcion == "F":
        print("Fin del programa.")
        continuar = False
    else:
        print("Opción no válida.")


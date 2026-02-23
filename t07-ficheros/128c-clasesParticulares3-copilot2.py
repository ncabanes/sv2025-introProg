import os

ARCHIVO = "clases.txt"


# ---------------------------------------------------------
# Cargar datos desde archivo de texto
# ---------------------------------------------------------
def cargar_datos():
    clases = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    nombre, fecha, hora, importe = linea.split("#")
                    clases.append({
                        "nombre": nombre,
                        "fecha": fecha,
                        "hora": hora,
                        "importe": float(importe)
                    })
    return clases


# ---------------------------------------------------------
# Guardar datos en archivo de texto
# ---------------------------------------------------------
def guardar_datos(clases):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for c in clases:
            linea = f"{c['nombre']}#{c['fecha']}#{c['hora']}#{c['importe']}"
            f.write(linea + "\n")


# ---------------------------------------------------------
# Añadir clase
# ---------------------------------------------------------
def anadir_clase(clases):
    nombre = input("Nombre del alumno: ")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")

    nueva = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "importe": 0.0
    }

    clases.append(nueva)
    guardar_datos(clases)
    print("Clase añadida correctamente.")
    return clases


# ---------------------------------------------------------
# Ver clases pendientes
# ---------------------------------------------------------
def ver_pendientes(clases):
    print("CLASES PENDIENTES:")
    pendientes = 0

    for i, clase in enumerate(clases, start=1):
        if clase["importe"] == 0:
            pendientes += 1
            print(f"{i}. {clase['fecha']} {clase['hora']} - {clase['nombre']}")

    if pendientes == 0:
        print("No hay clases pendientes.")


# ---------------------------------------------------------
# Marcar clase como impartida
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Calcular estadísticas
# ---------------------------------------------------------
def calcular_importes(clases):
    cantidad = len(clases)
    total = 0

    for c in clases:
        total += c["importe"]

    media = total / cantidad if cantidad > 0 else 0

    print("ESTADÍSTICAS:")
    print(f"Total de clases: {cantidad}")
    print(f"Importe total: {total:.2f}")
    print(f"Importe medio por clase: {media:.2f}")


# ---------------------------------------------------------
# Modificar clase
# ---------------------------------------------------------
def modificar_clase(clases):
    numero = int(input("Número de clase a modificar: "))
    valido = numero >= 1 and numero <= len(clases)

    if valido:
        clase = clases[numero - 1]

        nueva_fecha = input(f"Fecha [{clase['fecha']}]: ")
        nueva_hora = input(f"Hora [{clase['hora']}]: ")
        nuevo_nombre = input(f"Nombre [{clase['nombre']}]: ")
        nuevo_importe = input(f"Importe [{clase['importe']}]: ")

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


# ---------------------------------------------------------
# Menú principal
# ---------------------------------------------------------
def mostrar_menu():
    print("===== GESTIÓN DE CLASES PARTICULARES =====")
    print("A - Añadir nueva clase")
    print("P - Ver clases pendientes")
    print("I - Marcar clase como impartida")
    print("T - Calcular importe total y media")
    print("M - Modificar una clase")
    print("F - Fin")


def main():
    clases = cargar_datos()
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Elige una opción: ").upper()

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


if __name__ == "__main__":
    main()

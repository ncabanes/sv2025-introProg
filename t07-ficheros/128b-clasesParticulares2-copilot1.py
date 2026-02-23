import json
import os

ARCHIVO = "clases.json"


# ---------------------------------------------------------
# 1. Cargar datos al iniciar
# ---------------------------------------------------------
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# ---------------------------------------------------------
# 2. Guardar datos tras cada cambio
# ---------------------------------------------------------
def guardar_datos(clases):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(clases, f, indent=4, ensure_ascii=False)


# ---------------------------------------------------------
# 3. Añadir nueva clase
# ---------------------------------------------------------
def anadir_clase(clases):
    nombre = input("Nombre del alumno: ")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")

    nueva = {
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "importe": 0
    }

    clases.append(nueva)
    guardar_datos(clases)
    print("Clase añadida correctamente.")
    return clases


# ---------------------------------------------------------
# 4. Ver clases pendientes
# ---------------------------------------------------------
def ver_pendientes(clases):
    print("\nCLASES PENDIENTES:")
    hay_pendientes = False

    for i, clase in enumerate(clases, start=1):
        if clase["importe"] == 0:
            hay_pendientes = True
            print(f"{i}. {clase['fecha']} {clase['hora']} - {clase['nombre']}")

    if not hay_pendientes:
        print("No hay clases pendientes.")


# ---------------------------------------------------------
# 5. Marcar clase como impartida
# ---------------------------------------------------------
def marcar_impartida(clases):
    numero = int(input("Número de clase impartida: "))

    if numero < 1 or numero > len(clases):
        print("Número incorrecto.")
        return clases

    clase = clases[numero - 1]

    if clase["importe"] != 0:
        print("Esa clase ya tenía un importe asignado.")
        return clases

    importe = float(input("Importe cobrado: "))
    clase["importe"] = importe

    guardar_datos(clases)
    print("Clase marcada como impartida.")
    return clases


# ---------------------------------------------------------
# 6. Calcular estadísticas
# ---------------------------------------------------------
def calcular_importes(clases):
    if not clases:
        print("No hay clases registradas.")
        return

    total = sum(c["importe"] for c in clases)
    cantidad = len(clases)
    media = total / cantidad if cantidad > 0 else 0

    print("\nESTADÍSTICAS:")
    print(f"Total de clases: {cantidad}")
    print(f"Importe total: {total:.2f}")
    print(f"Importe medio por clase: {media:.2f}")


# ---------------------------------------------------------
# 7. Modificar una clase
# ---------------------------------------------------------
def modificar_clase(clases):
    numero = int(input("Número de clase a modificar: "))

    if numero < 1 or numero > len(clases):
        print("Número incorrecto.")
        return clases

    clase = clases[numero - 1]

    print("Introduce los nuevos datos (deja vacío para mantener el valor actual):")

    nueva_fecha = input(f"Fecha [{clase['fecha']}]: ")
    nueva_hora = input(f"Hora [{clase['hora']}]: ")
    nuevo_nombre = input(f"Nombre [{clase['nombre']}]: ")
    nuevo_importe = input(f"Importe [{clase['importe']}]: ")

    if nueva_fecha:
        clase["fecha"] = nueva_fecha
    if nueva_hora:
        clase["hora"] = nueva_hora
    if nuevo_nombre:
        clase["nombre"] = nuevo_nombre
    if nuevo_importe:
        clase["importe"] = float(nuevo_importe)

    guardar_datos(clases)
    print("Clase modificada correctamente.")
    return clases


# ---------------------------------------------------------
# 8. Menú principal
# ---------------------------------------------------------
def mostrar_menu():
    print("""
===== GESTIÓN DE CLASES PARTICULARES =====
A - Añadir nueva clase
P - Ver clases pendientes
I - Marcar clase como impartida
T - Calcular importe total y media
M - Modificar una clase
F - Fin
""")


def main():
    clases = cargar_datos()

    while True:
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
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

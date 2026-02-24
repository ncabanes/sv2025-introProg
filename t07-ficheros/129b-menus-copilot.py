import json
import os

FICHERO = "menus.json"


# ---------------------------------------------------------
# 1. Cargar datos desde archivo
# ---------------------------------------------------------
def cargar_datos():
    if os.path.exists(FICHERO):
        with open(FICHERO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# ---------------------------------------------------------
# 2. Guardar datos en archivo
# ---------------------------------------------------------
def guardar_datos(menus):
    with open(FICHERO, "w", encoding="utf-8") as f:
        json.dump(menus, f, indent=4, ensure_ascii=False)


# ---------------------------------------------------------
# 3. Añadir un nuevo menú
# ---------------------------------------------------------
def anadir_menu(menus):
    fecha = input("Fecha (YYYY-MM-DD): ")
    primer = input("Primer plato: ")

    # Validación: segundo plato distinto del primero
    while True:
        segundo = input("Segundo plato: ")
        if segundo.lower() != primer.lower():
            break
        print("El segundo plato no puede ser igual que el primero.")

    # Validación: calorías no negativas
    while True:
        try:
            calorias = int(input("Calorías: "))
            if calorias >= 0:
                break
            print("Las calorías no pueden ser negativas.")
        except ValueError:
            print("Introduce un número válido.")

    nuevo = {
        "fecha": fecha,
        "primer": primer,
        "segundo": segundo,
        "calorias": calorias
    }

    menus.append(nuevo)
    guardar_datos(menus)
    print("Menú añadido correctamente.")
    return menus


# ---------------------------------------------------------
# 4. Ver menús entre dos fechas
# ---------------------------------------------------------
def ver_entre_fechas(menus):
    f_ini = input("Fecha inicial (YYYY-MM-DD): ")
    f_fin = input("Fecha final (YYYY-MM-DD): ")

    print("\nMenús entre", f_ini, "y", f_fin)
    print("----------------------------------")

    for i, m in enumerate(menus):
        if f_ini <= m["fecha"] <= f_fin:
            print(f"{i}. {m['fecha']} - {m['primer']} / {m['segundo']}")


# ---------------------------------------------------------
# 5. Buscar texto en los platos
# ---------------------------------------------------------
def buscar_texto(menus):
    texto = input("Texto a buscar: ").lower()

    print("\nResultados de búsqueda:")
    print("------------------------")

    for i, m in enumerate(menus):
        if texto in m["primer"].lower() or texto in m["segundo"].lower():
            print(f"{i}. {m['fecha']} - {m['primer']} / {m['segundo']}")


# ---------------------------------------------------------
# 6. Calcular calorías medias
# ---------------------------------------------------------
def calorias_medias(menus):
    if not menus:
        print("No hay menús registrados.")
        return

    total = sum(m["calorias"] for m in menus)
    cantidad = len(menus)
    media = total / cantidad

    print("\nCálculo de calorías:")
    print("----------------------")
    print("Cantidad de menús:", cantidad)
    print("Calorías totales:", total)
    print("Media:", media)


# ---------------------------------------------------------
# 7. Modificar un menú existente
# ---------------------------------------------------------
def modificar_menu(menus):
    try:
        num = int(input("Número de menú a modificar: "))
    except ValueError:
        print("Número inválido.")
        return menus

    if num < 0 or num >= len(menus):
        print("No existe un menú con ese número.")
        return menus

    print("Introduce los nuevos datos:")

    fecha = input("Fecha (YYYY-MM-DD): ")
    primer = input("Primer plato: ")

    while True:
        segundo = input("Segundo plato: ")
        if segundo.lower() != primer.lower():
            break
        print("El segundo plato no puede ser igual que el primero.")

    while True:
        try:
            calorias = int(input("Calorías: "))
            if calorias >= 0:
                break
            print("Las calorías no pueden ser negativas.")
        except ValueError:
            print("Introduce un número válido.")

    menus[num] = {
        "fecha": fecha,
        "primer": primer,
        "segundo": segundo,
        "calorias": calorias
    }

    guardar_datos(menus)
    print("Menú modificado correctamente.")
    return menus


# ---------------------------------------------------------
# 8. Menú principal
# ---------------------------------------------------------
def mostrar_menu():
    print("""
===== GESTIÓN DE MENÚS DEL HOSPITAL =====
A - Acabar
B - Añadir menú
C - Ver menús entre fechas
D - Buscar texto en los platos
E - Calorías medias
F - Modificar menú
""")


def main():
    menus = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip().upper()

        if opcion == "A":
            print("Saliendo del programa.")
            break
        elif opcion == "B":
            menus = anadir_menu(menus)
        elif opcion == "C":
            ver_entre_fechas(menus)
        elif opcion == "D":
            buscar_texto(menus)
        elif opcion == "E":
            calorias_medias(menus)
        elif opcion == "F":
            menus = modificar_menu(menus)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

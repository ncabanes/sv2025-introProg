# Colección de coches, versión 1

def mostrar_menu():
    print("1. Añadir un coche")
    print("2. Ver todos")
    print("0. Terminar")

def cargar() -> list:
    coches = []
    # Los datos van a ser: "Ford:Mustang"
    try:
        fichero = open("coches.txt", "r")
        linea = fichero.readline().rstrip()
        while linea:
            trozos = linea.split(":")
            marca = trozos[0]
            modelo = trozos[1]
            coches.append({
                "marca" : marca,
                "modelo" : modelo })
            linea = fichero.readline().rstrip()
        fichero.close()
    except:
        print("No había datos, los voy a crear")
    return coches


def anadir(coches : list) -> list:
    marca = input("Dime la marca: ")
    modelo = input("Dime el modelo: ")
    coches.append({
        "marca" : marca,
        "modelo" : modelo })
    return coches


def mostrar(coches : list) -> None:
    for coche in coches:
        print(coche["marca"], "-", coche["modelo"])


def guardar(coches : list) -> None:
    fichero = open("coches.txt", "w")
    for coche in coches:
        fichero.write(coche["marca"] + ":" + coche["modelo"] + "\n")
    fichero.close()


# ---------- Cuerpo del programa --------

coches = cargar()
terminado = False
while not terminado:
    mostrar_menu()
    opcion = input("Opcion? ")
    
    if opcion == "0":
        terminado = True
    elif opcion == "1":
        coches = anadir(coches)
    elif opcion == "2":
        mostrar(coches)
    else:
        print("Opción incorrecta")

guardar(coches)
print("Hasta otra")

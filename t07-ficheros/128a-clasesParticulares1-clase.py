def cargar() -> list:
    clases = []
    try:
        f = open("clases.txt", "r")
        linea = f.readline().rstrip()
        while linea:
            trozos = linea.split(";")
            clases.append({
                "nombre": trozos[0],
                "fecha": trozos[1],
                "hora": trozos[2],
                "importe": int(trozos[3])
                })
            linea = f.readline().rstrip
        f.close()
    except:
        print("No habia archivo de guardado, creandolo")
    return clases

def guardar(clases: list) -> None:
    f = open("clases.txt", "w")
    for i in range(len(clases)):
        f.write(clases[i]["nombre"] + ";" + clases[i]["fecha"] +
            ";" + clases[i]["hora"] + ";" + str(clases[i]["importe"]) + 
            "\n")
    f.close()

def mostrar_menu() -> None:
    print("MENU")
    print("1.- Añadir clase")
    print("2.- Ver clases pendientes")
    print("3.- Marcar clase como impartida")
    print("4.- Importe total de las clases")
    print("5.- Modificar clase")
    print("F.- Fin")

def anadir(clases: list) -> list:
    nombre = input("Dime el nombre del alumno: ")
    fecha = input("Fecha de la clase (AAAA-MM-DD): ")
    hora = input("Hora de la clase (HH:MM): ")

    clases.append({
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "importe": 0
        })
    return clases

def ver_pendientes(clases: list) -> None:
    for i in range(len(clases)):
        if clases[i]["importe"] == 0:
            print(i+1, clases[i]["fecha"], "-", 
            clases[i]["hora"], "-", clases[i]["nombre"])

def marcar_clase(clases: list) -> None:
    num = int(input("Que clase quieres marcar como impartida: ")) - 1
    if num >= 0 and num < len(clases):
        if clases[num]["importe"] == 0:
            n_importe = int(input("Que importe le quieres poner a esa clase: "))
            clases[num]["importe"] = n_importe
        else:
            print("Esa clase ya se ha impartido y tiene un importe ya definido")
    else:
        print("Ese numero de clase no existe")
            
def importe_total(clases: list) -> None:
    total = 0
    contador = 0
    for i in range(len(clases)):
        importe = int(clases[i]["importe"])
        total += importe
        contador += 1
    print("El total de ingresos por todas las clases es de:", total)
    media = total / contador
    print("La media de los ingresos de todas las clases es de:", media)

def modificar(clases: list) -> list:
    num = int(input("Que clase quieres modificar: ")) - 1
    if num >= 0 and num < len(clases):
        n_nombre = input("Dime el nombre del alumno: ")
        n_fecha = input("Fecha de la clase (AAAA-MM-DD): ")
        n_hora = input("Hora de la clase (HH:MM): ")
        n_importe = int(input("Importe de la clase: "))

        clases[num] = {
            "nombre": n_nombre,
            "fecha": n_fecha,
            "hora": n_hora,
            "importe": n_importe
            }
    else:
        print("Ese numero de clase no existe")
    return clases

clases = cargar()
terminado = False
while not terminado:
    mostrar_menu()
    opcion = input("Que quieres hacer: ").upper()
    if opcion == "1":
        anadir(clases)
        guardar(clases)
    elif opcion == "2":
        ver_pendientes(clases)
    elif opcion == "3":
        marcar_clase(clases)
        guardar(clases)
    elif opcion == "4":
        importe_total(clases)
    elif opcion == "5":
        modificar(clases)
        guardar(clases)
    elif opcion == "F":
        print("Saliendo")
        terminado = True

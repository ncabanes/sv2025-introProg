# Contabilidad: descripción, fecha (AAAA-MM-DD), importe
# Opciones: añadir, ver todos (+total), borrar

def guardar(gastos: list) -> None:
    fichero = open("gastos.dat", "w")
    for g in gastos:
        fichero.write(g["descripc"]+"~"+g["fecha"]+"~"+str(g["importe"])+"\n")
    fichero.close()

def cargar() -> list:
    gastos =  []
    try:
        fichero = open("gastos.dat", "r")
        linea = fichero.readline().rstrip()
        while linea:
            trozos = linea.split("~")
            gastos.append({
                "descripc" : trozos[0],
                "fecha" : trozos[1],
                "importe" : float(trozos[2])
            })
            linea = fichero.readline().rstrip()
        fichero.close()
    except:
        print("No había datos, se creará un fichero nuevo")
    return gastos

def mostrar_menu() -> None:
    print()
    print("1- Añadir un gasto")
    print("2- Ver gastos")
    print("3- Borrar un gasto")
    print("T- Terminar")

def anadir(gastos: list) -> list:
    descripcion = input("Descripción del gasto? ")
    fecha = input("Fecha del gasto (AAAA-MM-DD)? ")
    importe = float(input("Importe del gasto? "))
    
    gastos.append({
        "descripc" : descripcion,
        "fecha" : fecha,
        "importe" : importe
    })
    return gastos

def ver(gastos: list) -> None:
    total = 0
    for i in range(len(gastos)):
        g = gastos[i]
        print(str(i+1) + ": " + g["descripc"] + ", de " + \
            g["fecha"] + ": " + str(g["importe"]))
        total += g["importe"]
    print("Total: ",total)

def borrar(gastos: list) -> list:
    numero = int(input("Gasto a borrar? ")) - 1
    del gastos[numero]
    # Alternativo:
    # gastos.remove(gastos[numero])
    return gastos


# ------ Cuerpo del programa -------
gastos = cargar()
terminado = False
while not terminado:
    mostrar_menu()
    opcion = input("Opción? ").upper()
    if opcion == "1":
        gastos = anadir(gastos)
    elif opcion == "2":
        ver(gastos)
    elif opcion == "3":
        gastos = borrar(gastos)
    elif opcion == "T":
        terminado = True
    else:
        print("Opción no válida")
        
guardar(gastos)

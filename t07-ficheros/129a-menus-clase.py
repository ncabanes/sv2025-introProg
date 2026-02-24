# Lista de menús

def cargar() -> list:
    menus = []
    try:
        with open("menus.txt", "r") as fichero:
            for linea in fichero:
                fragmento = linea.rstrip().split("#")
                    
                menus.append({
                    "primero" : fragmento[0], 
                    "segundo" : fragmento[1],
                    "fecha" : fragmento[2],
                    "calorias" : int(fragmento[3])
                })
    except:
        print("Fichero no encontrado, se creará uno")
            
    return menus


def guardar(menus: list) -> None:
    with open("menus.txt", "w") as fichero:
        for i in range(len(menus)):
            fichero.write(menus[i]["primero"]+"#")
            fichero.write(menus[i]["segundo"]+"#")
            fichero.write(menus[i]["fecha"]+"#")
            fichero.write(str(menus[i]["calorias"])+"\n")
            
        
def mostrar_menu() -> None:
    print()
    print("-------------Comedor-------------")
    print("1. Añadir menú")
    print("2. Ver menus entre fechas" )
    print("3. Buscar")
    print("4. Calcular calorias medias")
    print("5. Modificar menú")
    print("A. Acabar")
    

def anadir(menus: list) -> list:
    primero = input("Nombre del primer plato? ")
    segundo = input("Nombre del segundo plato? ")
    
    while primero.lower() == segundo.lower():
        print("Repetido, vuelve a introducir el segundo plato")
        segundo = input("Nombre del segundo plato? ")
        
    fecha = input("Fecha? ")
    calorias = input("Calorias? ")
    
    menus.append({
        "primero" : primero, 
        "segundo" : segundo,
        "fecha" : fecha,
        "calorias" : calorias
    })
        
    return menus
    

def ver_entre_fechas(menus: list) -> None:
    fecha_inicial = input("Fecha inicial? ")
    fecha_final = input("Fecha final? ")
    
    for i in range(len(menus)):
        if menus[i]["fecha"] >= fecha_inicial and menus[i]["fecha"] <= fecha_final:
            print(i+1, menus[i]["fecha"], "1º:", menus[i]["primero"],
                "2º:",menus[i]["segundo"])


def buscar(menus: list) -> None:
    texto = input("Texto a buscar? ")
    
    for i in range(len(menus)):
        if texto.lower() in menus[i]["primero"].lower() \
                or texto.lower() in menus[i]["segundo"].lower():
            print(i+1, menus[i]["fecha"], "1º:", menus[i]["primero"],
                "2º:",menus[i]["segundo"])


def total_calorias(menus: list) -> None:
    calorias_totales = 0
    for i in range(len(menus)):
        calorias_totales += int(menus[i]["calorias"])
        
    print("Cantidad de menús:", len(menus), " - Calorias totales:",
        calorias_totales, " - Media: ", calorias_totales/len(menus))
    

def modificar(menus: list) -> list:
    n_menu = int(input("Número del menú? "))-1
    
    if n_menu >= 0 and n_menu <= len(menus):
        nuevo_primero = input("Nombre del primer plato? ")
        nuevo_segundo = input("Nombre del segundo plato? ")
        nuevo_fecha = input("Fecha? ")
        nuevo_calorias = input("Calorias? ")
        
        menus[n_menu] = {
            "primero" : nuevo_primero, 
            "segundo" : nuevo_segundo,
            "fecha" : nuevo_fecha,
            "calorias" : nuevo_calorias
        }
    else:
        print("Menú no encontrado")
            
    return menus
    
    
#--------------Cuerpo del programa-------------------

menus = cargar()    
terminado = False

while not terminado:
    mostrar_menu()
    
    opc = input("Elige una opción: ").upper()
    
    if opc == "1":      #Añadir menus
        anadir(menus)
        guardar(menus)
    elif opc == "2":    #Ver menus entre dos fechas
        ver_entre_fechas(menus)
    elif opc == "3":    #Buscar en los menus
        buscar(menus)
    elif opc == "4":    #Calcular calorias medias
        total_calorias(menus)
    elif opc == "5":    #Modificar menu
        modificar(menus)
        guardar(menus)
    elif opc == "A":    #Acabar
        print("Hasta otra...")
        terminado = True
    else:
        print("Opción no valida")

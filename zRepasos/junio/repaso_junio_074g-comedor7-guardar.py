# Repaso para Junio 74 (semana del 25/05 al 31/05)
# 
# (Este ejercicio es un ejemplo de cómo podría ser el examen final 
# "grande", valorado de 0 a 10).
# 
# El servicio de comedor de un pequeño hospital te ha pedido que les 
# ayudes a apuntar los menús que van realizando, para evitar repetirse.
# 
# Para cada menú desean apuntar el nombre del primer plato (por ejemplo, 
# "crema de zanahorias"), el nombre del segundo plato (por ejemplo, "lomo 
# en salsa"), la fecha (como texto, por ejemplo, "2026-02-20") y las 
# calorías estimadas (un número sin decimales).
# 
# El programa debe:
# 
# 1. Mostrar un menú que recuerde al usuario todas las opciones 
# disponibles y se repita hasta que se escoja la opción "A" (Acabar), que 
# deberá ser aceptable tanto en mayúsculas como en minúsculas. (1 punto) 
# 
# 2. Permitir añadir un nuevo menú, que se guardará en formato de 
# diccionario, y que a su vez será parte de una lista llamada "menus". 
# Para cada menú se le pedirá fecha, primer plato, segundo plato y 
# calorías. Si el segundo plato, por error, se introduce igual que el 
# primer plato, se deberá volver a pedir, tantas veces como sea 
# necesario. (2 puntos) 
# 
# 3. Poder ver los menús que ha habido entre dos fechas (por ejemplo, 
# entre  "2026-02-16" y "2026-02-20"). Se pedirá al usuario la fecha 
# inicial, y la fecha final y se mostrará número, fecha, primer plato y 
# segundo plato para todos los menús que tengan una fecha comprendida 
# entre ambas (inclusive). (1 punto)
#
# 4. Buscar los menús que contengan un cierto texto como parte del primer 
# plato o del segundo plato (independientemente de mayúsculas o 
# minúsculas). Se pedirá el texto a buscar y se mostrará número, fecha, 
# primer plato y segundo plato para todos los menús que tengan ese texto. 
# (1 punto)
# 
# 5. Calcular las calorías medias de los menús. Mostrará la cantidad de 
# menús, las calorías totales y la media (total dividido entre cantidad). 
# (1 punto) 
# 
# 6. Modificar los detalles de un menú, a partir de su número. Si el 
# número corresponde a un menú existente, se volverá a pedir su fecha, 
# primer plato, segundo plato y calorías. Si el número es incorrecto, se 
# avisara al usuario. Si las calorías son negativas, se deberán volver a 
# introducir tantas veces como sea necesario. (1 punto)
# 
# 7. Los datos se guardarán tras cada cambio (cuando se añada un menú o 
# se modifique). (1 punto)


def anyadir(menus: list) -> list:
    fecha = input("Dime la fecha del menú (AAAA-MM-DD): ")
    primero = input("Dime el primer plato del menú: ")
    segundo = input("Dime el segundo plato del menú: ")
    while segundo == primero:
        segundo = input("No debe repetirse. Dime el segundo plato del menú: ")
    calorias = int(input("Dime las calorías: "))
    
    menu = {
        "fecha": fecha,
        "primer_plato": primero,
        "segundo_plato": segundo,
        "calorias": calorias
    }
    menus.append(menu)
    return menus


def ver_entre_dos_fecha(menus: list) -> None:
    desde = input("Dime desde qué fecha (AAAA-MM-DD): ")
    hasta = input("Dime hasta qué fecha (AAAA-MM-DD): ")
    
    #for menu in menus:
    for i in range(len(menus)):
        menu = menus[i]
        if menu["fecha"] >= desde and menu["fecha"] <= hasta:
            print(i+1, menu["fecha"],
                menu["primer_plato"], menu["segundo_plato"])


def buscar(menus: list) -> None:
    texto = input("Texto a buscar: ")

    for i in range(len(menus)):
        menu = menus[i]
        if texto.upper() in menu["primer_plato"].upper() \
                or texto.upper() in menu["segundo_plato"].upper():
            print(i+1, menu["fecha"],
                menu["primer_plato"], menu["segundo_plato"])


def contar_calorias(menus: list) -> None:
    calorias = 0
    for menu in menus:
        calorias += menu["calorias"]
    
    print("Calorías totales:", calorias)
    print("Cantidad de menús:", len(menus))
    print("Calorías medias:", calorias / len(menus))


def modificar(menus: list) -> list:
    numero = int(input("¿Número de menú a modificar? "))-1
    
    if numero >= 0 and numero < len(menus):
        fecha = input("Dime la fecha del menú (AAAA-MM-DD): ")
        primero = input("Dime el primer plato del menú: ")
        segundo = input("Dime el segundo plato del menú: ")
        calorias = int(input("Dime las calorías: "))
        while calorias < 0:
            calorias = int(input("Dime las calorías: "))
        
        menu = {
            "fecha": fecha,
            "primer_plato": primero,
            "segundo_plato": segundo,
            "calorias": calorias
        }
        menus[numero] = menu
    else:
        print("Número de menú no válido")
    return menus


def guardar(menus: list) -> None:
    fichero = open("menus.txt", "w")
    #fichero.write("Hola\n")
    for menu in menus:
        fichero.write(menu["fecha"]+";"+
            menu["primer_plato"]+";"+
            menu["segundo_plato"]+";"+
            str(menu["calorias"])+"\n")
    fichero.close()

# ------------ Cuerpo del programa ----------

menus = [ ]
terminado = False
while not terminado:
    print()
    print("1- Añadir menú")
    print("2- Ver menús entre 2 fechas")
    print("3- Buscar un texto")
    print("4- Calorias medias")
    print("5- Modificar un menú")
    print("A- Acabar")
    opcion = input("Dime una opción: ").upper()
    
    if opcion == "1":
        menus = anyadir(menus)
        guardar(menus)
    elif opcion == "2":
        ver_entre_dos_fecha(menus)
    elif opcion == "3":
        buscar(menus)
    elif opcion == "4":
        contar_calorias(menus)
    elif opcion == "5":
        menus = modificar(menus)
        guardar(menus)
    elif opcion == "A":
        terminado = True

print("Hasta luego")

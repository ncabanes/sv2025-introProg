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


# ------------ Cuerpo del programa ----------


menus = [ ]
terminado = False
while not terminado:
    print("1- Añadir menú")
    print("2- Ver menús entre 2 fechas")
    print("A- Acabar")
    opcion = input("Dime una opción: ").upper()
    
    if opcion == "1":
        menus = anyadir(menus)
    elif opcion == "A":
        terminado = True

print("Hasta luego")

# 61.- Un amigo tuyo ha decidido dar clases particulares de inglés y te 
# ha pedido que le ayudes a apuntar qué clases tiene pendientes.
# 
# Para cada clase quiere apuntar el nombre del alumno, la fecha (como 
# texto, por ejemplo, "2026-02-16") y la hora (como texto, por ejemplo 
# "19:05"). Además, cuando ya ha impartido la clase (pero no antes) 
# quiere poder anotar cuánto ha cobrado por ella.
# 
# El programa debe:
# 
# 1. Mostrar un menú que recuerde al usuario todas las opciones 
# disponibles y se repita hasta que se escoja la opción "F" (Fin), ya sea 
# en mayúsculas o en minúsculas. (1 punto) 

# Versión 1: sólo menú

terminado = False
while not terminado:
    print("1- Añadir una clase")
    print("2- Ver clases pendientes")
    print("3- Marcar clase como impartida")
    print("4- Calcular importe de las clases")
    print("5- Modificar una clase")
    print("F- Fin")
    
    opcion = input("¿Qué opción? ").upper()
    
    # if opcion == "F" or opcion == "f":
    if opcion == "F":
        terminado = True

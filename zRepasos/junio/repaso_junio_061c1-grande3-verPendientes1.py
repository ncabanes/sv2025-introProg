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
# 
# 2. Permitir añadir un nueva clase, que se guardará en formato de 
# diccionario, y que a su vez será parte de una lista llamada "clases". 
# Para cada clase, se le pedirá nombre, fecha y hora, y el importe se 
# anotará como 0 (para indicar que está pendiente) (2 puntos) 
# 
# 3. Poder ver las clases pendientes (las que tienen importe 0). Para 
# cada clase, se mostrará su número (contando desde 1), su fecha, su hora 
# y el nombre del alumno. (1 punto)


# Versión 3: menú + añadir + ver

terminado = False
clases =  [ ]
while not terminado:
    print("1- Añadir una clase")
    print("2- Ver clases pendientes")
    print("3- Marcar clase como impartida")
    print("4- Calcular importe de las clases")
    print("5- Modificar una clase")
    print("F- Fin")
    
    opcion = input("¿Qué opción? ").upper()
    
    if opcion == "F":
        terminado = True

    elif opcion == "1": # Añadir
        nombre = input("Dime el nombre del alumno: ")
        fecha = input("Dime la fecha de la clase: ")
        hora = input("Dime la hora de la clase: ")
        
        clase =  {
            "alumno": nombre,
            "fecha": fecha,
            "hora": hora,
            "importe": 0
        }
        clases.append( clase )
    
    elif opcion == "2": # Ver
        for clase in clases:
            if clase["importe"] == 0:
                print(clase["fecha"], 
                    clase["hora"], 
                    clase["alumno"])

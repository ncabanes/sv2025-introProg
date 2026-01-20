# Crea un programa que permita al usuario guardar una recopilación de 
# refranes. Le permitirá añadir un refrán, ver todos los refranes 
# existentes u ordenarlos alfabéticamente. Existirá un menú que permita 
# escoger una de esas acciones y que se repetirá hasta que se elija la 
# opción de Terminar.

refranes = [ ]
terminado = False

while not terminado  :

    print("1 - Añadir un refrán")
    print("2 - Ver todos los refranes")
    print("3 - Ordenar alfabéticamente")
    print("T - Terminar")
    
    opcion = input().upper()
    
    if opcion == "1":
        # refranes.append(input("Refrán: "))
        refran = input("Refrán: ")
        refranes.append(refran)
        
    elif opcion == "2":
        #print(refranes)
        for r in refranes:
            print(r)

    elif opcion == "3":
        refranes.sort()

    elif opcion == "T":
        terminado = True

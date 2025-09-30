# Ejercicio 18. Nombre del día de la semana (V2)

# Pide al usuario el número de un día de la semana (del 1 al 7) y 
# respóndele el nombre del día (por ejemplo, "martes"). En esta
# versión debes emplear "elif" ...

dia = int(input("Dime el dia? "))
if dia == 1:
    print("Es lunes")
elif dia == 2:
        print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
        print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
        print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("no valido")
        

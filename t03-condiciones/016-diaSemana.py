# Ejercicio 16. Nombre del día de la semana

# Pide al usuario el número de un día de la semana (del 1 al 7) y 
# respóndele el nombre del día (por ejemplo, "martes"). Debes 
# emplear if + else + if + ...


diasem = int(input("Dime el número de un día de la semana: "))

if diasem == 1:
    print("Es lunes")
else:
    if diasem == 2:
        print("Es martes")
    else:
        if diasem == 3:
            print("Es miércoles")
        else:
            if diasem == 4:
                print("Es jueves")
            else:
                if diasem == 5:
                    print("Es viernes")
                else:
                    if diasem == 6:
                        print("Es sábado")
                    else:
                        if diasem == 7:
                            print("Es domingo")
                        else:
                            print("Ese día no existe")

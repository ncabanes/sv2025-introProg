# 2A - 1ev - Ejercicio 2

# 2. Crea un programa que pida al usuario un número de mes (del 1 al 12) y le 
# responda cuántos días tiene, en un año no bisiesto (los meses 1, 3, 5, 7, 8, 10 
# y 12 tienen 31 días; los meses 4, 6, 9 y 11 tienen 30 días; el mes 2 tiene 28 
# días). Debe repetirse hasta que escriba un número de mes no válido (0 o menor 
# que 12).

valido = True
while valido:
    mes = int(input("Introduce un número de mes (1-12): "))
    
    if mes == 0 or mes > 12:
        print("Número de mes no válido. Fin del programa.")
        valido = False
    else:
        if mes == 2:
            print("28 días")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("30 días")
        else:
            print("31 días")

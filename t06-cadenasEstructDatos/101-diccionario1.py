dias_mes = {
    "enero" : 31,
    "febrero" : 28,
    "marzo" : 31,
}

print(dias_mes["enero"])

mes = input("Dime el nombre de un mes: ").lower()

if mes in dias_mes:
    print(dias_mes[ mes ])

    print("Los días de",mes,"son",dias_mes[ mes ])

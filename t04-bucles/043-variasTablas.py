# Varias tablas de multiplicar

desde = int(input("Desde qué tabla? "))
hasta = int(input("Hasta qué tabla? "))

for tabla in range(desde, hasta+1):   
    print("Tabla del", tabla)
    for numero in range(0, 11):
        print(tabla, "x", numero,"=", tabla*numero)
    print()

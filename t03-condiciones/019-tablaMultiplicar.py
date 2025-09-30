# 19. Tabla de multiplicar

# Crea un programa que pregunte al usuario un número del 0 al 10 y muestre su 
# tabla de multiplicar (por ejemplo, para el número 5, deberá escribir desde "5
# x 0 = 0" hasta "5 x 10 = 50"). Si el número introducido está por debajo de 0
# o por encima de 10, deberá responder con un mensaje de error.

tabla = int(input("Qué tabla de multiplicar quieres? "))
if tabla >= 0 and tabla <= 10:
    print(tabla, " x 0 = ", tabla*0)
    print(tabla, " x 1 = ", tabla*1)
    print(tabla, " x 2 = ", tabla*2)
    print(tabla, " x 3 = ", tabla*3)
    print(tabla, " x 4 = ", tabla*4)
    print(tabla, " x 5 = ", tabla*5)
    print(tabla, " x 6 = ", tabla*6)
    print(tabla, " x 7 = ", tabla*7)
    print(tabla, " x 8 = ", tabla*8)
    print(tabla, " x 9 = ", tabla*9)
    print(tabla, " x 10 = ", tabla*10)
else:
    print("No conozco esa tabla")

# Alternativa:

#if tabla < 0 or tabla > 10:
#    print("No conozco esa tabla")
#else:
#    ...
    

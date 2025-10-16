# 19. Tabla de multiplicar

# Crea un programa que pregunte al usuario un número del 0 al 10 y muestre su 
# tabla de multiplicar (por ejemplo, para el número 5, deberá escribir desde "5
# x 0 = 0" hasta "5 x 10 = 50"). Si el número introducido está por debajo de 0
# o por encima de 10, deberá responder con un mensaje de error.

tabla = int(input("Qué tabla de multiplicar quieres? "))
if tabla >= 0 and tabla <= 10:
    for numero in range(0, 11):
        print(f"{tabla} x {numero} = {tabla*numero}")
else:
    print("No conozco esa tabla")

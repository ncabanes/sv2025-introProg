# Repaso para junio 14

# Haz un programa que pregunte al usuario 
# dos números reales (con decimales) y responda 
# "El primero es el mayor", "El segundo es el 
# mayor" o "Los dos son iguales", según 
# corresponda.


n1 = float(input("Dime el primer número: "))
n2 = float(input("Dime el segundo número: "))

if n1 > n2:
    print("El primero es el mayor")
else:
    if n2 > n1:
        print("El segundo es el mayor")
    else:
        print("Los dos son iguales")

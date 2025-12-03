# 3. Pide 5 números enteros al usuario. Después de que introduzca cada 
# uno, debes decirle si es par o no lo es.

for i in range(5):
    n = int(input("Dime un número: "))
    
    if n % 2 == 0:
        print("Es par")
    else:
        print("No es par")

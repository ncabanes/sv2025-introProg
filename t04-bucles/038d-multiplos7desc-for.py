# Variante:  Crea un programa que pida al usuario 2 números enteros y muestre todos los que hay desde el primero hasta el segundo, de forma descendente. Además, debe avisar de cuáles son múltiplos de 7, así:
# 
# Desde? 100
# Hasta? 10
# 100
# 99
# 98 Múltiplo de 7
# 97
# 96
# ...

desde = int(input("Desde? "))
hasta = int(input("Hasta? "))

for i in range(desde, hasta-1, -1):
    if i % 7 == 0 :
        print(i, "Múltiplo de 7")
    else:
        print(i)

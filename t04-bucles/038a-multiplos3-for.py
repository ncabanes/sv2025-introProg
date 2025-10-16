# Crea un programa que pida al usuario 2 números enteros y muestre todos los que hay desde el primero hasta el segundo. Además, debe avisar de cuáles son múltiplos de 3, así:
# 
# Desde? 150
# Hasta? 160
# 150 Múltiplo de 3
# 151
# 152
# 153 Múltiplo de 3
# 154
# 155
# ...

desde = int(input("Desde? "))
hasta = int(input("Hasta? "))
for i in range(desde, hasta+1):
    print(i)
    if i % 3 == 0:
        print("Múltiplo de 3")

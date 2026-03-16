# Repaso para junio 16

# 16. Pide al usuario un número 
# del 1 al 5 y respóndele su nombre 
# ("uno", "dos", "tres"...).

n = int(input("¿Qué número?  "))

if n == 1:
    print("uno")
elif n == 2:
    print("dos")
elif n == 3:
    print("tres")
elif n == 4:
    print("cuatro")
elif n == 5:
    print("cinco")
else:
    print("Sólo del 1 al 5, por favor")

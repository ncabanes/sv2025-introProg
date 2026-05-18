# Repaso para junio 65

# 65.- Pide al usuario dos números enteros. Respóndele cuántas veces es 
# mayor uno que el otro. Por ejemplo, si los números son 2 y 12 (o 12 y 
# 2), deberás responder "12 es 6 veces mayor que 2".

n1 = int(input("Dime un número entero: "))
n2 = int(input("Dime otro número entero: "))
    
if n1 > n2:
    veces = n1 // n2
    print(n1,"es",veces,"veces mayor que",n2)
else:
    veces = n2 // n1
    print(n2,"es",veces,"veces mayor que",n1)

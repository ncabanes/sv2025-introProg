# Pide dos números reales al usuario y respóndele cuántos son 
# positivos (dos, uno o ninguno)

n1 = float(input("dime un numero? "))
n2 = float(input("dime otro? "))
if n1 >= n2:
    print("el mayor es", n1)
else:
    print("el mayor es", n2)

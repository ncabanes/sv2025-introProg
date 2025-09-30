# 21. Cantidad de positivos

# Pide dos números reales al usuario y respóndele 
# cuántos son positivos (dos, uno o ninguno)

n1 = float(input("dime un numero? "))
n2 = float(input("dime otro? "))
if n1 > 0 and n2 > 0:
    print("Los dos son positivos")
elif n1 > 0 or n2 > 0:
    print("Solo uno es positivo")
else:
    print("Ninguno es positivo")

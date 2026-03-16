# Repaso para junio 18

# Pide al usuario que introduzca dos veces 
# el mismo número. Si no lo hace correctamente, 
# vuélveselo a pedir otras dos veces, tanto como
# sea necesario.

n1 = int(input("Dime el número: "))
n2 = int(input("Vuelve a introducirlo: "))

while n1 != n2:
    print("Debe ser el mismo")
    
    n1 = int(input("Dime el número: "))
    n2 = int(input("Vuelve a introducirlo: "))

print("Lo has conseguido")

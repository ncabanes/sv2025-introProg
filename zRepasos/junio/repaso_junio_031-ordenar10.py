# Repaso para junio 31

# Pide al usuario 10 números y 
# luego muéstralos ordenados

numeros = [ ]

for i in range(10):
    numeros.append( float(input("Dime un número: ")) )

numeros.sort()

for n in numeros:
    print(n, end=" ")

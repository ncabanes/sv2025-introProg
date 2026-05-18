# Repaso para junio 64

# 64.- Pide al usuario un número par. Si el número no es par, dile 
# "Vaya!" y termina la ejecución. En caso contrario, pregúntale cuántas 
# veces quiere incrementar a partir de él, y mostrarás tantos números 
# pares como te hayan indicado. Por ejemplo, si el número es el 10 y 
# quiere incrementar 3 veces a partir de él, tu programa debería 
# escribir: 
# 10
# 12 
# 14
# 16

numero = int(input("Dime un número par: "))
if numero % 2 != 0:
    print("Vaya!")
else:
    veces = int(input("¿Cuántas veces lo incrementamos? "))
    for i in range(veces+1):
        print(numero + i * 2)
    

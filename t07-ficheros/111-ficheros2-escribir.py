suma = 0
fichero = open("multiplosDe7.txt", "r") 
linea = fichero.readline().rstrip() 
while linea: 
    numero = int(linea)
    suma += numero
    linea = fichero.readline().rstrip() 
fichero.close()
print(suma)

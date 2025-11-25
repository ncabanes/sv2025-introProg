# Pide al usuario datos numéricos, hasta que introduzca un 0 para indicar 
# que desea terminar. Entonces muéstrale la media y los datos que están 
# por encima de la media.

datos = []

numero = int (input("Dime un número: "))
while numero != 0:
	datos.append(numero)
	numero = int (input("Dime otro número: "))

suma = 0
for n in datos:
	suma += n
media = suma / len(datos)
print("La media es", media)

print("Por encima de la media: ", end="")
for n in datos:
	if n > media:
		print(n, end=" ")

#for i in range(len(datos)):
#	if datos[i] > media:
#		print(datos[i], end=" ")

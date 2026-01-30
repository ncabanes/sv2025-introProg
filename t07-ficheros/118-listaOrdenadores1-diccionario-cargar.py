# Lista de ordenadores

ordenadores = [ ]

f = open("ordenadores.txt", "r")

linea = f.readline().rstrip()
while linea:
	#print(linea)
	fragmentos = linea.split("#")
	nombre = fragmentos[0]
	anyo = int(fragmentos[1])
	ordenadores.append({
		"nombre" : nombre,
		"año": anyo })
	linea = f.readline().rstrip()
f.close()


	
seguir = True

while seguir:
	print()
	print("1- Añadir")
	print("2- Ver")
	print("3- Modificar")
	print("S- Salir")
	
	opcion = input("Opción? ").lower()
	
	if opcion == "1":
		nombre = input("Nombre? ")
		anyo = int(input("Año? "))
		ordenadores.append({
			"nombre" : nombre,
			"año": anyo })

	elif opcion == "2":
		#print(ordenadores)
		
		#for o in ordenadores:
		#	print(o)
		
		for i in range(len(ordenadores)):
			print(i+1, ordenadores[i]["nombre"],
				ordenadores[i]["año"])

	elif opcion == "3":
		numero = int(input("Número de ordenador? ")) - 1
		nombre = input("Nombre? ")
		anyo = int(input("Año? "))
		ordenadores[numero] = {
			"nombre" : nombre,
			"año": anyo }

	elif opcion == "s":
		seguir = False
	else:
		print("Opción no válida")

f = open("ordenadores.txt", "w")
for o in ordenadores:
	f.write(o["nombre"]+"#"+str(o["año"])+"\n")
f.close()

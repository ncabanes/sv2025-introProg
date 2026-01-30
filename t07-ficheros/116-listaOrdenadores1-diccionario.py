# Lista de ordenadores

ordenadores = [{
	"nombre" : "ZxSpectrum",
	"año": 1982 }]
	
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

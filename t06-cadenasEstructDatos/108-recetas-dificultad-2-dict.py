recetas =  [
	{ "nombre" : "Macarrones con tomate",
		"dificultad" : 1 },
	{ "nombre" : "Judías con chorizo",
		"dificultad" : 3 },
]

terminado = False

while not terminado:
	
	print("1- Añadir una receta")
	print("2- Ver todas las recetas")
	print("3- Modificar una receta")
	print("S- Salir")

	opcion = input("Opcion: ").upper()
	
	if opcion == "1": # Añadir
		receta = input("Nombre de la receta? ")
		dificultad = int(input("Dificultad de la receta (1 a 5)? "))
		
		nueva_receta = { "nombre" : receta,
			"dificultad" : dificultad }
		
		recetas.append(nueva_receta)
		
	elif opcion == "2":  # Mostrar todas
		for i in range(len(recetas)):
			receta = recetas[i]
			print(i+1, ":", receta["nombre"],
				"-", receta["dificultad"])
				
			#print(i+1, ":", recetas[i]["nombre"],
			#	"-", recetas[i]["dificultad"])
			
	elif opcion == "3":  # Modificar
		numero_receta = int(input("Qué número de receta? "))-1
		receta = input("Nuevo nombre de la receta? ")
		dificultad = int(input("Dificultad de la receta (1 a 5)? "))

		recetas[numero_receta] = { "nombre" : receta,
			"dificultad" : dificultad }

	elif opcion == "S":
		terminado = True

	else:
		print("Opción incorrecta")


print("Hasta otra...")

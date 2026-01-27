nombres_recetas =  [ ]
dificultades_recetas =  [ ]

terminado = False

while not terminado:
	
	print("1- Añadir una receta")
	print("2- Ver todas las recetas")
	print("3- Modificar una receta")
	print("S- Salir")

	opcion = input("Opcion: ").upper()
	
	if opcion == "1": # Añadir
		receta = input("Nombre de la receta? ")
		nombres_recetas.append(receta)
		dificultad = int(input("Dificultad de la receta (1 a 5)? "))
		dificultades_recetas.append(dificultad)
		
	elif opcion == "2":  # Mostrar todas
		for i in range(len(nombres_recetas)):
			print(i+1, ":", nombres_recetas[i],
				"-", dificultades_recetas[i])
			
	elif opcion == "3":  # Modificar
		numero_receta = int(input("Qué número de receta? "))-1
		receta = input("Nuevo nombre de la receta? ")
		nombres_recetas[numero_receta] = receta
		dificultad = int(input("Dificultad de la receta (1 a 5)? "))
		dificultades_recetas[numero_receta] = dificultad

	elif opcion == "S":
		terminado = True

	else:
		print("Opción incorrecta")


print("Hasta otra...")

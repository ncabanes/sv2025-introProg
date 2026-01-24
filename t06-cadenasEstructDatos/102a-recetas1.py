recetas =  [ ]

print("1- Añadir")
print("2- Ver")
print("3- Ordenar")
print("S- Salir")

opcion = input("Opcion").upper()

while opcion != "S":
	
	if opcion == "1":
		receta = input("Nombre de la receta? ")
		recetas.append(receta)
		#recetas.append( input("Nombre de la receta? "))
	elif opcion == "2":
		for r in recetas:
			print(r)
	elif opcion == "3":
		recetas.sort()
	elif opcion != "S":
		print("Opción incorrecta")
	
	print("1- Añadir")
	print("2- Ver")
	print("3- Ordenar")
	print("S- Salir")

	opcion = input("Opcion").upper()

print("Hasta otra...")

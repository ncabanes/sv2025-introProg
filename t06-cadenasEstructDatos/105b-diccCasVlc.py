diccio = {
	"ventana" : "finestra",
	"puerta" : "porta"
}

terminado = False

while not terminado:
	
	print()
	print("1- Añadir una palabra")
	print("2- Buscar una palabra")
	print("3- (Intentar) Traducir una frase")
	print("S- Salir")

	opcion = input("Opcion: ").upper()
	
	if opcion == "1": # Añadir palabra
		castellano = input("Dime la palabra en castellano: ")
		valenciano = input("Dime su traducción a valenciano: ")
		diccio [ castellano ] = valenciano
		
	elif opcion == "2":  # Buscar una palabra
		castellano = input("Dime la palabra en castellano: ")
		if castellano in diccio:
			print(diccio [ castellano ])
		else:
			print("Palabra desconocida")
			
	elif opcion == "3":  # Traducir una frase
		frase = input("Dime la frase: ")
		palabras = frase.split()
		for palabra in palabras:
			if palabra in diccio:
				print(diccio [ palabra ], end = " ")
			else:
				print(palabra, end = " ")
		print()

	elif opcion == "S":
		terminado = True

	else:
		print("Opción incorrecta")


print("Hasta otra...")

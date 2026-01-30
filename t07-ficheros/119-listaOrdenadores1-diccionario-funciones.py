# Lista de ordenadores

def guardar(ordenadores: list) -> None:
	f = open("ordenadores.txt", "w")
	for o in ordenadores:
		f.write(o["nombre"]+"#"+str(o["año"])+"\n")
	f.close()

def cargar() -> list:
	ordenadores = []
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
	return ordenadores

def mostrar(ordenadores :list) -> None:
	#print(ordenadores)
	
	#for o in ordenadores:
	#	print(o)
	
	for i in range(len(ordenadores)):
		print(i+1, ordenadores[i]["nombre"],
			ordenadores[i]["año"])

def anadir(ordenadores: list) -> list:
	nombre = input("Nombre? ")
	anyo = int(input("Año? "))
	ordenadores.append({
		"nombre" : nombre,
		"año": anyo })
	return ordenadores

def modificar(ordenadores: list) -> list:
	numero = int(input("Número de ordenador? ")) - 1
	nombre = input("Nombre? ")
	anyo = int(input("Año? "))
	ordenadores[numero] = {
		"nombre" : nombre,
		"año": anyo }
	return ordenadores

def mostrar_menu() -> None:
	print()
	print("1- Añadir")
	print("2- Ver")
	print("3- Modificar")
	print("S- Salir")

# --------- Cuerpo del programa ------

ordenadores = cargar()

seguir = True

while seguir:
	mostrar_menu()
	
	opcion = input("Opción? ").lower()
	if opcion == "1":
		ordenadores = anadir(ordenadores)
	elif opcion == "2":
		mostrar(ordenadores)
	elif opcion == "3":
		ordenadores = modificar(ordenadores)
	elif opcion == "s":
		seguir = False
	else:
		print("Opción no válida")

guardar(ordenadores)

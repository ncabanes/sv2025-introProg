# A partir de la lista de días de la semana, pide al usuario 
# el nombre de un día y dile si es un nombre válido o no lo es.

dias = ["lunes", "martes", "miércoles", "jueves", "viernes",
	"sábado", "domingo"]

nombre_buscar = input("Dime el nombre de un día: ")

encontrado = False
for dia in dias:
	if dia == nombre_buscar:
		encontrado = True

if encontrado:
	print("Existe")
else:
	print("No existe")

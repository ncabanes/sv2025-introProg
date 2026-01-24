notas_us_esp = {
	"A": "Sobresaliente",
	"B": "Notable",
	"C": "Bien",
	"D": "Suficiente",
	"F": "Suspenso"
}

print("F es:", notas_us_esp["F"])

nota = input("Qué nota estadounidense? ").upper()
if nota in notas_us_esp:
	print(notas_us_esp[ nota ])
else:
	print("Nota no válida")

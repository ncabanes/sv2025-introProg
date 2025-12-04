# 8.  Crea una función escribir_iniciales,
# que reciba como parámetro un nombre 
# (una cadena de texto) y escriba su primera 
# letra y cada letra que encuentre después 
# de un espacio.


def escribir_iniciales(texto: str) -> None:
	print(texto[0], end="")
	for i in range(1, len(texto)):
		if texto[i] == " ":
			print(texto[i+1], end="")

escribir_iniciales("Cayo Julio César")
escribir_iniciales("Billy Bob Thornton")
escribir_iniciales("Hideo Kojima")

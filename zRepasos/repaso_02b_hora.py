# 2. Pregunta la hora (un número entero) al usuario, respóndele buenos 
# días si el número está entre el 6 y 13, buenas tardes y está entre 14 y 
# 20 y buenas noches si es a partir de 21 o antes de 6.

hora = int(input("Dime la hora: "))

if hora >= 6 and hora <= 13:
	print("Buenos días")
elif hora >=14 and hora <= 20:
	print("Buenas tardes")
else:
	print("Buenas noches")

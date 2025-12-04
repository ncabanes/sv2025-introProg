# 1. Pregunta al usuario su nombre y su año de nacimiento, deduce su edad 
# restando 2025 del año de nacimiento y respóndele algo como "Hola, 
# Nacho, así que tienes 20 años".

nombre = input("Dime tu nombre: ")
anyo = int(input("Año de nacimiento: "))

edad = 2025 - anyo
print("Hola,", nombre, ", así que tienes",
	edad, "años")

#print("Hola, " + nombre + ", así que tienes " +
#	str(edad) + " años")

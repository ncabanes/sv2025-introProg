# Para una competición deportiva, queremos guardar los tiempos (en 
# segundos, con decimales) que 8 deportistas han tardado en completar una 
# cierta prueba. Luego queremos mostrar el tiempo de la persona más 
# rápida

tiempos = []

for i in range(8):
	tiempo = float(input("Dime el tiempo: "))
	tiempos.append( tiempo )

print("Más rápido:", min(tiempos))

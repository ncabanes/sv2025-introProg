# 7.  Crea una función cantidad_de_cifras, 
# que reciba como parámetro un número entero
# y devuelva la cantidad de cifras que tiene. 
# Puedes deducirla dividiendo entre 10 tantas 
# veces como sea necesario hasta que su 
# parte entera se convierta en cero.

def cantidad_de_cifras(n: int) -> int:
	divisiones = 0
	while n != 0:
		divisiones += 1
		n //= 10
	return divisiones

print(cantidad_de_cifras(567))

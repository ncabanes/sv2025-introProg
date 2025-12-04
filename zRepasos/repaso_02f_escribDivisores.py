# 6.  Diseña una función escribir_divisores,
# que muestre los divisores del numero 
# entero que se le pase como parámetro, 
# cada uno en una linea.

def escribir_divisores(n: int) -> None:
	for i in range(1,n+1):
		if n % i == 0:
			print(i)

escribir_divisores(48)

# 5.  Prepara una función triplicar, que reciba 
# como parámetro un número real y devuelva 
# el resultado de multiplicarlo por 3.

def triplicar(n: float) -> float:
	return n * 3

x = triplicar(5)
if x == 15:
	print("Ok")
else:
	print("La ca*aste")

print(triplicar(10))

# Crea una función llamada MCD, que devuelva el máximo común divisor 
# de los dos números enteros que se le pasen como parámetro.

def MCD(n1: int, n2: int) -> int:
    if n1 < n2:
        menor = n1
    else:
        menor = n2
    
    maximo = 0
    for i in range(1, menor+1):
        if n1 % i == 0 and n2 % i == 0:
            maximo = i
    return maximo

print("MCD(20,15) =", MCD(20,15))
print("MCD(5,6) =", MCD(5,6))
print("MCD(200,2000) =", MCD(200, 2000))

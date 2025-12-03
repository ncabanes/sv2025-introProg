# 4. Crea una función "diferencia_de_cuadrados", que tenga como 
# parámetros dos números reales "a" y "b", que devuelva el valor de 
# a²-b². Crea otra función "suma_por_diferencia", que tenga como 
# parámetros dos números reales "a" y "b", que devuelva el valor de 
# (a+b)*(a-b). En el cuerpo del programa, comprueba tres veces (con 
# números inventados por ti) si ambas funciones dan el mismo resultado 
# (cuando los parámetros son los mismos, claro).

def diferencia_de_cuadrados(a : float, b : float) -> float:
    return a*a - b*b

def suma_por_diferencia(a : float, b : float) -> float:
    return (a+b)*(a-b)

print(diferencia_de_cuadrados(10,2) == suma_por_diferencia(10,2))
print(diferencia_de_cuadrados(-3,0) == suma_por_diferencia(-3,0))
print(diferencia_de_cuadrados(1.5,2.3) == suma_por_diferencia(1.5,2.3))

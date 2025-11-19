# Crea una función "escribir_triangulo_nombre", que reciba un nombre 
# como "Marc" y escriba algo como:
# 
# M
# Ma
# Mar
# Marc

def escribir_triangulo_nombre(nombre: str) -> None:
    for i in range(len(nombre)):
        print(nombre[0:i+1])

escribir_triangulo_nombre("Francisco")

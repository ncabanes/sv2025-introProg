# Crea una función "escribirRectangulo", que dibuje un rectángulo relleno, 
# con el ancho, alto y carácter que se indiquen como parámetros 

def escribirRectangulo(ancho, alto, caracter):
    for fila in range(alto):
        for columna in range(ancho):
            print(caracter, end="")
        print()

escribirRectangulo(20, 5, '*')
print()
escribirRectangulo(30, 7, "#")

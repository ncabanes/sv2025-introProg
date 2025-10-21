# Crea una función "escribirRectangulo", que dibuje un rectángulo relleno, 
# con el ancho, alto y carácter que se indiquen como parámetros 

# (V2: variante más compacta)

def escribirRectangulo(ancho, alto, caracter):
    for fila in range(alto):
        print(caracter * ancho)

escribirRectangulo(20, 5, '*')
print()
escribirRectangulo(30, 7, "#")

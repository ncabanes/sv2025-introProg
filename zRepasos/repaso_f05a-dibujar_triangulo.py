"""
1. Crea y prueba una función "dibujar_triangulo", que recibirá como parámetros el tamaño del triángulo
 y el carácter de relleno. Dibujará un triángulo relleno alineado a la izquierda, con el tamaño 
 y carácter que se indiquen. Por ejemplo, si el tamaño es 4 y el carácter es "$", debería escribir:

$
$$
$$$
$$$$
"""

def dibujar_triangulo(tamano, caracter):
    for i in range(1, tamano + 1):
        print(caracter * i)

dibujar_triangulo(4, "$")

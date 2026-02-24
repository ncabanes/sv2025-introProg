"""
1. Crea y prueba una función "dibujar_rectangulo_hueco", que 
reciba como parámetros el ancho y el alto del rectángulo, así
como el carácter con el que se quiere dibujar. Por ejemplo,
si ancho=8, alto=4, caracter="$", debería escribir:

$$$$$$$$
$      $
$      $
$$$$$$$$
"""

def dibujar_rectangulo_hueco(ancho: int, alto: int , caracter: str) -> None:
    print(caracter * ancho)
    for i in range(alto - 2):
        print(caracter + " " * (ancho - 2) + caracter)
    print(caracter * ancho)

dibujar_rectangulo_hueco(8, 4, "$")

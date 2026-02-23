# Función "dibujar_rectangulo(ancho, alto, caracter)": 
# escribiría un recuadro relleno con el ancho, alto y carácter
# que se indiquen. Por ejemplo, si ancho=10, alto=3, caracter="$", 
# debería escribir:
# 
# $$$$$$$$$$
# $$$$$$$$$$
# $$$$$$$$$$

def dibujar_rectangulo(ancho: int, alto: int, caracter: str) -> None:
    for i in range(alto):
        print(caracter * ancho)

dibujar_rectangulo(10, 3, "$")

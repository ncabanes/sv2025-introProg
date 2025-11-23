# Crea una función "escribir_recuadro_hueco(ancho,alto,caracter)", que escriba un 
# recuadro hueco, con el ancho, alto y carácter que se indiquen como parámetros.

def escribir_recuadro_hueco(ancho,alto,caracter):
    for fila in range(0, alto):
        for columna in range(0, ancho):
            if fila == 0 or fila == alto-1 or columna == 0 or columna == ancho-1:
                print(caracter, end="")
            else:
                print(" ", end="")
        print()

escribir_recuadro_hueco(10, 5, "X")
    

# Crea una función "escribir_recuadro_hueco(ancho,alto,caracter)", que escriba un 
# recuadro hueco, con el ancho, alto y carácter que se indiquen como parámetros.

def escribir_recuadro_hueco(ancho : int, alto : int, caracter : str) -> None:
    # Primera fila
    print(caracter * ancho)
    
    # Filas intermedias
    for fila in range(0, alto-2):
        print(caracter + " "*(ancho-2) + caracter)
        
    # Última fila
    print(caracter * ancho)

escribir_recuadro_hueco(10, 5, "X")
    

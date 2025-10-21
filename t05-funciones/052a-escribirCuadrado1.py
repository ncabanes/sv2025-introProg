# Función escribirCuadrado 

# Escribe un cuadrado relleno, con el tamaño (ancho y alto) 
# que se indique como primer parámetros, y el símbolo que se
# indique como segundo parámetro

def escribirCuadrado(tamanyo, simbolo):
    for fila in range(tamanyo):
        for columna in range(tamanyo):
            print(simbolo, end="")
        print()


escribirCuadrado(15, '*')
print()
escribirCuadrado(20, "#")


# Función escribirCuadrado (V2: variante más compacta)

# Escribe un cuadrado relleno, con el tamaño (ancho y alto) 
# que se indique como primer parámetros, y el símbolo que se
# indique como segundo parámetro

def escribirCuadrado(tamanyo, simbolo):
    for fila in range(tamanyo):
        print(simbolo * tamanyo)


escribirCuadrado(15, '*')
print()
escribirCuadrado(20, "#")


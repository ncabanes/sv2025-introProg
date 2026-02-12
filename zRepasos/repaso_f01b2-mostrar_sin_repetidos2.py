# Crea una función "mostrar_sin_repetidos", que a partir de 
# una lista como [5, 4, 5, 4, 1, 2, 1, 2, 3] escriba en 
# pantalla algo como "5 4 1 2 3".

# Versión 2: usa conjuntos. Más rápida y más compacta,
# pero no muestra los datos en su orden original

def mostrar_sin_repetidos(lista: list) -> None:
    no_repetidos = set(lista)
    for respuesta in no_repetidos:
        print(respuesta, end=" ")    
    
mostrar_sin_repetidos([5, 4, 5, 4, 1, 2, 1, 2, 3])

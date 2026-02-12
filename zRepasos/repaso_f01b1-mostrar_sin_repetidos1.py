# Crea una función "mostrar_sin_repetidos", que a partir de 
# una lista como [5, 4, 5, 4, 1, 2, 1, 2, 3] escriba en 
# pantalla algo como "5 4 1 2 3".

def mostrar_sin_repetidos(lista: list) -> None:
    no_repetidos = [ ] 
    for n in lista:
        if not n in no_repetidos:
            no_repetidos.append(n)
    
    for respuesta in no_repetidos:
        print(respuesta, end=" ")
    
    
mostrar_sin_repetidos([5, 4, 5, 4, 1, 2, 1, 2, 3])

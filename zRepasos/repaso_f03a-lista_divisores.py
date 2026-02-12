# Función "lista_divisores(n)": devolverá la lista de 
# divisores de un número entero. Por ejemplo, si el 
# número es 8, debería devolver la lista [1, 2, 4, 8].

def lista_divisores(n: int) -> list:
    lista = [ ]
    for i in range(1, n+1):
        if n%i == 0:
            lista.append(i)

    return lista
    
print(lista_divisores(8))

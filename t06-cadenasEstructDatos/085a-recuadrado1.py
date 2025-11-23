# Crea una función "escribir_recuadrado(nombre : str)", que escriba 
# un nombre (que se le indique como parámetro) con un recuadro alrededor.

# Versión 1: con caracteres disponibles en el teclado

def escribir_recuadrado(nombre : str) -> None:
    print("-" * (len(nombre)+2))
    print("|"+nombre+"|")
    print("-" * (len(nombre)+2))

escribir_recuadrado("Gonzalo")
    

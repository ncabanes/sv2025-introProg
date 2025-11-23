# Crea una función "escribir_recuadrado(nombre : str)", que escriba 
# un nombre (que se le indique como parámetro) con un recuadro alrededor.

# Versión 2: con caracteres Unicode

def escribir_recuadrado(nombre : str) -> None:
    print("┌"+"─" * len(nombre)+"┐")
    print("│"+nombre+"│")
    print("└"+"─" * len(nombre)+"┘")

escribir_recuadrado("Gonzalo")
    

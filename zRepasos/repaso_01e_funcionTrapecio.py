# 5. Crea una función "escribir_trapecio", que reciba como parámetros 
# la base mayor (que será la de arriba) y la altura, y dibuje un trapecio 
# con ese tamaño. Por ejemplo, si la base mayor es 10 y la altura es 4, 
# debería dibujar algo como:
# 
# **********
#  ********
#   ******
#    ****

def escribir_trapecio(base_mayor : int, altura : int) -> None:

    asteriscos = base_mayor
    espacios = 0

    for i in range(altura):
        print(espacios * " ", asteriscos * "*", sep="")
        espacios += 1
        asteriscos -= 2

escribir_trapecio(10,4)

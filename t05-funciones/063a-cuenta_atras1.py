# Crea una función "escribir_cuenta_atras", que escriba una cuenta atrás desde
# el número que se le indique como parámetro hasta 0, cada número en una línea.

# Versión 1, sin type hinting

def escribir_cuenta_atras(desde):
    for i in range(desde, -1, -1):
        print(i)

escribir_cuenta_atras(10)

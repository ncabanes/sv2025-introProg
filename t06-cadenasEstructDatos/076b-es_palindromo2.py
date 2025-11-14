# Es palíndromo un texto?

# Versión 2, con una comparación rápida usando subcadenas

def es_palindromo(texto):
    return texto == texto[::-1] 

if es_palindromo("level"):
    print("Vamos bien")

if es_palindromo("ayer"):
    print('Falla con "ayer"')

if not es_palindromo("ADA"):
    print('Falla con "ADA"')

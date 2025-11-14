# Es palíndromo un texto?

def es_palindromo(texto):
    invertido = ""
    for i in range(len(texto)-1, -1, -1):
        invertido += texto[i]
    # Forma de comprobar, si parece fallar:
    # print("Resultado: ", invertido)

    if texto == invertido:
        return True
    else:
        return False

    # Forma alternativa, más compacta, de devolver el valor
    # return texto == invertido
    

if es_palindromo("level"):
    print("Vamos bien")

if es_palindromo("ayer"):
    print('Falla con "ayer"')

if not es_palindromo("ADA"):
    print('Falla con "ADA"')

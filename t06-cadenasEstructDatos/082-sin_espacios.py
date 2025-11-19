# Crea una función "sin_espacios(texto)", que reciba un texto
# y lo devuelva sin espacios en blanco intermedios.

def sin_espacios(texto: str) -> str:
    # respuesta = ""
    # for letra in texto:
    #     if letra != " ":
    #         respuesta += letra
    # return respuesta

    return texto.replace(" ","")

print(sin_espacios("1 2 3   A B"))

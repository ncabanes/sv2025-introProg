# Repaso para junio 71

# 71.- Crea una función "extraer_las_que_comienzan", que reciba una 
# lista de palabras y una letra. Devolverá una lista (quizá vacía) que 
# contenga las palabras que empiezan por esa letra (quizá con mayúsculas 
# distintas). Por ejemplo si las palabras de la lista son "hola" y 
# "Adiós" y la letra es "a", debería devolverte una lista formada 
# únicamente por la palabra "Adiós".

def extraer_las_que_comienzan(lista: list, letra: str) -> list:
    resultado =  [ ]
    for palabra in lista:
        if palabra[0].upper() == letra.upper():
            resultado.append(palabra)
    return resultado

palabras = ["Hola", "Adios", "mañana", "ayer"]
print( extraer_las_que_comienzan(palabras, "a") )

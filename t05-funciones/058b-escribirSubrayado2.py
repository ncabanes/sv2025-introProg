# Crea una función "escribir_subrayado", que reciba como parámetro un texto
# y lo escriba subrayado con guiones (pista: puedes saber la longitud  
# -cantidad de letras- de un texto con len(texto).

# Versión 2: con "type hinting" y con lógica distinta (cadena * número en
# vez de "for")

def escribir_subrayado(texto : str):
    print(texto)
    print("-" * len(texto) )

escribir_subrayado("Hola")


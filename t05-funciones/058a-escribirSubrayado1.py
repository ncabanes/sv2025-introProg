# Crea una función "escribir_subrayado", que reciba como parámetro un texto
# y lo escriba subrayado con guiones (pista: puedes saber la longitud  
# -cantidad de letras- de un texto con len(texto).

# Versión 1: sin "type hinting"

def escribir_subrayado(texto : str):
    print(texto)
    for i in range(len(texto)):
        print("-", end="")

escribir_subrayado("Hola")

#for i in range(1, len(texto)+1)
#for i in range(0, len(texto))
#for i in range(len(texto))

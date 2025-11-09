# Crea una función "es_vocal", que reciba un símbolo y 
# devuelva True si es una vocal, o False si no lo es.

# Versión 2, devolviendo el valor de la condición

def es_vocal(letra: str) -> bool:
    return letra=='a' or  letra=='e' or letra=='i' \
            or letra=='o' or letra=='u'

print("a es una vocal?", es_vocal("a"))
print("b es una vocal?", es_vocal("b"))

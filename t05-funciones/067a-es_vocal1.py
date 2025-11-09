# Crea una función "es_vocal", que reciba un símbolo y 
# devuelva True si es una vocal, o False si no lo es.

# Versión 1, con "if"

def es_vocal(letra: str) -> bool:
    if letra=='a' or  letra=='e' or letra=='i' \
            or letra=='o' or letra=='u':
        return True
    else:
        return False

if es_vocal("a"):
    print("a es una vocal")
else:
    print("a no es una vocal")

if es_vocal("b"):
    print("b es una vocal")
else:
    print("b no es una vocal")

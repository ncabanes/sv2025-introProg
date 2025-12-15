def es_primo_palindromo(n: int) -> bool:
    if es_primo(n) and es_palindromo(str(n)):
        return True
    else:
        return False

def es_primo(n: int) -> bool:
    divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False
    #return divisores == 2

def es_palindromo(t: str) -> bool:
    textoAlReves = t[::-1]
    if t == textoAlReves:
        return True
    else:
        return False

for i in range (1, 500):
    if es_primo_palindromo(i):
        print(i, end=" ")

import random

frases = [
    "el imperio contraataca",
    "la lista de schindler",
    "regreso al futuro",
    "al diablo con el diablo",
    "tootsie",
    "big",
    "sully",
    "esta casa es una ruina",
    "naufrago",
    "forrest gump",
    "polar express",
    "alien el octavo pasajero",
    "el proyecto de la bruja de blair",
    "el caballero oscuro",
    "terminator salvation",
    "star trek",
    "memento",
    "interstellar",
    "tenet",
    "it",
    "saw",
    "el resplandor",
    "psicosis",
    "los pajaros",
    "pesadilla en elm street",
    "krull",
]

num_frase = random.randint(0, len(frases) - 1)
frase_oculta = frases[num_frase]

frase_mostrar = ""
for c in frase_oculta:
    if c == " ":
        frase_mostrar += " "
    else:
        frase_mostrar += "-"

falladas = ""

errores = 0
max_errores = 5

print("¡Bienvenido al juego del Ahorcado!")
print("Adivina la película. Sólo se te permiten 5 fallos.")
print()

while errores < max_errores and "-" in frase_mostrar:
    print("Título:", frase_mostrar)
    print("Errores:", errores, "/", max_errores)
    print("Letras falladas:", falladas)
    
    letra = input("Introduce una letra: ").lower()
    print()

    if letra in frase_oculta.lower():
        proxima_frase_mostrar = ""
        for i in range(len(frase_oculta)):
            if frase_oculta[i].lower() == letra:
                proxima_frase_mostrar += frase_oculta[i]
            else:
                proxima_frase_mostrar += frase_mostrar[i]
        frase_mostrar = proxima_frase_mostrar

    else:
        falladas += letra
        errores += 1
        print("Lo siento, esa letra no está.")

# Fin del juego
if "-" not in frase_mostrar:
    print("¡Lo conseguiste!")
else:
    print("Has perdido. La palabra era:", frase_oculta)

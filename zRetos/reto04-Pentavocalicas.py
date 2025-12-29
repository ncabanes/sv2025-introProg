# Reto 04: Palabras pentavocálicas
# Acepta el reto, 300
# https://aceptaelreto.com/problem/statement.php?id=300

"""
Entrada
La entrada comienza con un número que indica la cantidad de casos de prueba
que vienen a continuación. Cada caso consiste en una palabra de no más de 30
letras de la a a la z (todas minúsculas, sin tilde y excluída la letra ñ).

Salida
Para cada caso de prueba, el programa escribirá SI si la palabra es
pentavocálica y NO en caso contrario.

Entrada de ejemplo
4
albaricoque
seculariza
peliagudo
abracadabra

Salida de ejemplo
SI
NO
SI
NO
"""

casos = int(input())

for i in range(casos):
    palabra = input()
    if "a" in palabra and "e" in palabra and "i" in palabra \
            and "o" in palabra and "u" in palabra:
        print("SI")
    else:
        print("NO")


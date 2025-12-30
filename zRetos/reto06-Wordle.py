# Reto 06: Wordle
# https://www.codechef.com/problems/WORDLE

"""
Wordle

Chef ha inventado un Wordle modificado: hay una palabra oculta S y una 
palabra intentada T, ambas de longitud 5.

Chef quiere crear una una cadena M de texto que refleje la exactitud de la 
palabra intentada. Para cada posición de M, si la letra es la misma en S y T, 
se mostrará la letra "G" o la letra "B" en caso contrario.

Formato de entrada
La primera línea contendrá T, el número de casos de prueba. A continuación, 
  se mostrarán los casos de prueba.
Cada caso de prueba consta de dos líneas de entrada.
La primera línea contiene la cadena S (la palabra oculta).
La ​​segunda línea contiene la cadena T (la palabra intentada).

Formato de salida
Para cada caso de prueba, debes mostrar el valor de la cadena M.

Ejemplo 1:
Entrada
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT

Salida
BBGBB
GBBBB
GGBBG

Explicación:
Caso de prueba 1: ABCDE y EDCBA. La cadena M es BBGBB, ya que solo la tercera letra es correcta.
Caso de prueba 2: ROUND y RINGS. La cadena M es GBBBB (solo la primera letra es correcta).
"""

N = int(input())

for i in range(N):
    S = input()
    T = input()

    M = ""

    for i in range(5):
        if S[i] == T[i]:
            M += "G"
        else:
            M += "B"

    print(M)

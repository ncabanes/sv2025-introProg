# Reto 02: Contando en la arena
# Acepta el reto, 369
# https://aceptaelreto.com/problem/statement.php?id=369

"""
Entrada
La entrada estará compuesta por distintos números mayores que 0 y 
que nunca serán mayores que 1.000, cada uno en una línea.
La entrada termina con un 0, que no debe procesarse.

Salida
Para cada número se debe escribir, en una línea independiente, 
su codificación en base 1.

Entrada de ejemplo
1
4
6
0

Salida de ejemplo
1
1111
111111
"""

# Versión 2: Con booleano de control

terminado = False
while not terminado:
	n = int(input())
	if n != 0:
		print (n * "1")
	else:
		terminado = True

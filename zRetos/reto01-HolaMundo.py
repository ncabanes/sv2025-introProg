# Reto 01: Hola Mundo
# Acepta el reto, 116
# https://aceptaelreto.com/problem/statement.php?id=116

"""
Escribir un programa que escriba tantos "hola mundo" como nos pidan.

Entrada
La entrada consta de una única línea que contiene un número n, 
0 ≤ n ≤ 5, que indica cuántos mensajes hay que emitir.

Salida
Cada mensaje a escribir aparecerá en una única línea y será la 
cadena "Hola mundo.".

Entrada de ejemplo
3

Salida de ejemplo
Hola mundo.
Hola mundo.
Hola mundo.
"""

n = int(input())

for i in range(n):
	print("Hola mundo.")

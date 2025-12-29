# Reto 03: Regalos

""" 
En la Navidad española, es posible recibir regalos el 25 de diciembre o el 
6 de enero, según las costumbres de cada familia.

Debes crear un programa que reciba varios pares de día y mes, y responda 
"Regalo" si es un día en el que quizá se reciban regalos o "No regalo" si es un 
día en el que es casi seguro que no se va a recibir ninguno.

Datos de entrada

En primer lugar recibirás un número, que indica cuantos pares de datos se van a 
analizar. Luego seguirán varias líneas formadas por un número de día (que será 
de 1 a 31, no hace falta validarlo) y un número de mes (de 1 a 12, tampoco es 
necesario validarlo), separados por un único espacio en blanco.

Ejemplo de entrada

5
23 12
6 1
25 12
9 1
28 12

Salida que se debería obtener con esa entrada:

No regalo
Regalo
Regalo
No regalo
No regalo
"""

# Versión 2: Parte cada línea en dos fragmentos y los analiza

n = int(input())

for _ in range(n):
    diaMes = input().split()
    dia = int(diaMes[0])
    mes = int(diaMes[1])
    if (dia == 25 and mes == 12) or (dia == 6 and mes == 1):
        print("Regalo")
    else:
        print("No regalo")

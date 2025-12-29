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

# Versión 1: Comprueba todo como una única cadena

n = int(input())

for i in range(n):
    diaMes = input()
    if diaMes == "25 12" or diaMes == "6 1":
        print("Regalo")
    else:
        print("No regalo")

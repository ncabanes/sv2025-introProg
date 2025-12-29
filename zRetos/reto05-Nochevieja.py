# Reto 05: Nochevieja
# Acepta el reto, 148
# https://www.aceptaelreto.com/problem/statement.php?id=148

"""
Ramón se pasa el día de Nochevieja contando los minutos que faltan para 
que den las uvas. ¿Puedes ayudarle?

Entrada
La entrada consiste en una serie de horas, cada una en una línea. Cada 
hora está formada por las horas y los minutos separados por : y 
utilizando siempre dos dígitos. Se utiliza una representación en formato 
24 horas (es decir, desde 00:00 a 23:59).

La entrada termina cuando la hora es la medianoche (00:00), que no debe 
procesarse.

Salida
Para cada caso de prueba se mostrará una línea con el número de minutos 
que faltan para medianoche.

Entrada de ejemplo
23:45
21:30
00:01
00:00

Salida de ejemplo
15
150
1439
"""

linea = input()
while linea != "00:00":

    fragmentos = linea.split(":")
    horas = int(fragmentos[0])
    minutos = int(fragmentos[1])

    minutos_pasados = horas * 60 + minutos
    restantes = 1440 - minutos_pasados

    print(restantes)

    linea = input()


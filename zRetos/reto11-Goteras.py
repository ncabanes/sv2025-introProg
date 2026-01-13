# Reto 11: Goteras
# Acepta el reto, 216
# https://www.aceptaelreto.com/problem/statement.php?id=216

"""
Con la llegada de las lluvias, has descubierto una molesta gotera en el salón. 
Con precisión suiza, las gotas caen una vez por segundo desde el techo hasta un 
improvisado cubo que te ves obligado a vaciar periódicamente hasta que 
encuentres una solución.

Convivir con una gotera es complicado porque tienes que sincronizar tu vida 
alrededor de los vaciados del cubo…

Entrada

La entrada estará compuesta de un primer número indicando cuántos casos de 
prueba vendrán a continuación.

Cada caso de prueba será un número mayor que cero con el número de gotas que 
entran en el cubo.


Salida

Para cada caso de prueba, el programa escribirá en una línea el tiempo máximo 
que puedes estar sin cambiar el cubo en el formato HH:MM:SS, donde HH indica el 
número de horas, MM el número de minutos y SS el número de segundos.

Ningún cubo es tan grande como para poder estar más de un día completo sin 
cambiarse.

Entrada de ejemplo
3
70
3600
3661
Salida de ejemplo
00:01:10
01:00:00
01:01:01
"""

def formatear(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

casos = int(input())
for i in range(casos):
    gotas = int(input())

    horas = gotas // 3600
    decenaHora = horas // 10
    unidadHora = horas % 10
    gotas = gotas % 3600
    
    minutos = gotas // 60
    decenaMinuto = minutos // 10
    unidadMinuto = minutos % 10
    gotas = gotas % 60
    
    decenaSegundo = gotas // 10
    unidadSegundo = gotas % 10

    print(decenaHora, unidadHora, ":",
        decenaMinuto, unidadMinuto, ":",
        decenaSegundo, unidadSegundo, sep="")

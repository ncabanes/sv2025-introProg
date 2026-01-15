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

casos = int(input())
for i in range(casos):
    gotas = int(input())
    
    horas = gotas // 3600
    gotas_restantes = gotas % 3600
    
    minutos = gotas_restantes // 60
    segundos = gotas_restantes % 60
    
    if horas < 10:
        print("0", end="")
    print(horas, end="")
    
    print(":", end="")
    
    if minutos < 10:
        print("0", end="")
    print(minutos, end="")
    
    print(":", end="")
    
    if segundos < 10:
        print("0", end="")
    print(segundos)
    
    pass

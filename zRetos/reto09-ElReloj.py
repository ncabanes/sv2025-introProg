# Reto 09: El reloj
# Concurso Tuenti, 2011,Reto 6 - El reloj

"""
Tienes un reloj digital de 7 segmentos LED. Un día, al despertar de un sueño de 
ciencia ficción, te preguntas: ¿cuántas veces se encenderán los LED 
individuales después de X segundos, desde la posición 00:00:00?

Ten en cuenta que cada segundo, todos los LED se apagan y luego se encienden 
los de la siguiente posición.

Entrada de ejemplo
0
4
1000
36000

Salida de ejemplo
36
172
30630
1069232
"""

def segmentos_encendidos(cifra: int) -> int:
    if cifra == 0:
        return 6
    elif cifra == 1:
        return 2
    elif cifra == 2:
        return 5
    elif cifra == 3:
        return 5
    elif cifra == 4:
        return 4
    elif cifra == 5:
        return 5
    elif cifra == 6:
        return 6
    elif cifra == 7:
        return 3
    elif cifra == 8:
        return 7
    elif cifra == 9:
        return 6

# Cuerpo del programa
linea = input()
while linea != "":
    segundosTotales = int(linea)
    respuesta = 0
    for segundoActual in range(segundosTotales+1):
        # print("S:", segundoActual)
        
        horas = segundoActual // 3600
        decenaHora = horas // 10
        unidadHora = horas % 10
        segundoActual = segundoActual % 3600
        
        minutos = segundoActual // 60
        decenaMinuto = minutos // 10
        unidadMinuto = minutos % 10
        segundoActual = segundoActual % 60
        
        decenaSegundo = segundoActual // 10
        unidadSegundo = segundoActual % 10
        #print("H:", decenaHora, unidadHora,
        #    decenaMinuto, unidadMinuto,
        #    decenaSegundo, unidadSegundo)
        
        respuesta = respuesta + \
            segmentos_encendidos(decenaHora) + \
            segmentos_encendidos(unidadHora) + \
            segmentos_encendidos(decenaMinuto) + \
            segmentos_encendidos(unidadMinuto) + \
            segmentos_encendidos(decenaSegundo) + \
            segmentos_encendidos(unidadSegundo) 

    print(respuesta)
    linea = input()

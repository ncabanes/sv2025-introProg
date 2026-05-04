# Repaso para junio 58

# (Ejemplo de examen de mínimos, 10/12)

# 58.- Pide al usuario que introduzca cadenas de texto, tantas como 
# quiera, que tú irás guardando en una lista. Cuando pulse Intro sin 
# teclear nada, terminará la introducción de datos y deberás comprobar si 
# la primera cadena coincide con alguna de las otras. Por ejemplo, si 
# coincide con la segunda, escribirás "Coincide que la 2". Si también 
# coincide con la quinta, escribirás "Coincide con la 5". Si no coincide 
# con ninguna, no es necesario que tu programa responda nada.

textos =  [ ]
frase = input("Dime un texto: ")
while frase != "":
    textos.append(frase)
    frase = input("Dime otro texto: ")

for i in range(1, len(textos)):
    if textos[0] == textos[i]:
        print("Coincide con la",i+1)

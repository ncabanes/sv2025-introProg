# Repaso para junio 59

# (Ejemplo de examen de mínimos, 11/12)

# 59.- Crea una versión mejorada del programa anterior: Pide al usuario 
# que introduzca cadenas de texto, tantas como quiera, que tú irás 
# guardando en una lista. Cuando pulse Intro sin teclear nada, terminará 
# la introducción de datos y deberás decir "La primera cadena está 
# repetida" o "La primera cadena no está repetida", según el caso.

# Primera aproximación, INCORRECTA: 
# avisar en el "else" de que no existe

textos =  [ ]
frase = input("Dime un texto: ")
while frase != "":
    textos.append(frase)
    frase = input("Dime otro texto: ")

for i in range(1, len(textos)):
    if textos[0] == textos[i]:
        print("Coincide con la",i+1)
    else:
        print("No está")

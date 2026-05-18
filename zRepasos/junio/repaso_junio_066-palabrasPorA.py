# Repaso para junio 66

# 66.- Pide al usuario que introduzca 6 palabras, guárdalas en una 
# lista y luego muestra las que comiencen por "a" (si es que hay alguna). 
# Si no hay ninguna, no hace falta que tu programa responda nada.

palabras = [ ]

for i in range(6):
    p = input("Dime una palabra: ")
    palabras.append(p)

for p in palabras:
    if p[0] == "a":
        print(p)

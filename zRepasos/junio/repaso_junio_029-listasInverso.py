# Repaso para junio 29

# Crea una lista con las palabras 
# "Uno", "Dos" y "Tres". Luego recórrela 
# en orden inverso, mostrando las 
# palabras que contiene, de la última 
# a la primera.

lista = [ "Uno", "Dos", "Tres" ]

print("La respuesta de verdad:")
for i in range(2,-1,-1):
    print(lista[i])

print()
print("Primer dato:", lista[0])
print("Los dos primeros:", lista[0:2])
print("Primero y tercero:", lista[0:3:2])
print("Todos al revés:", lista[::-1])

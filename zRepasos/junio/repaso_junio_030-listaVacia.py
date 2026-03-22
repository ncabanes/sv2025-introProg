# Repaso para junio 29

# Crea una lista vacía. Pide 
# 5 palabras al usuario y añádelas 
# a esa lista. Luego muestra la lista 
# en orden normal y finalmente en 
# orden inverso.

palabras = [ ]

for i in range(5):
    palabra = input("Dime una palabra: ")
    palabras.append(palabra)

print("En orden normal:")
for p in palabras:
    print(p)

print("En orden inverso:")
for i in range(4,-1,-1):
    print(palabras[i])

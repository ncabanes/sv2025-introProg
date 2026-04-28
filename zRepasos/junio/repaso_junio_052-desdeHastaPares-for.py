# Repaso para junio 52

# (Ejemplo de examen de mínimos, 4/12)

# 52.- Pide al usuario dos números enteros. Muestra los números pares 
# que van del menor de ellos al mayor de ellos, ambos incluidos, todos 
# ellos en la misma línea, separados por un espacio. Por ejemplo, si el 
# usuario introduce 8 y 3, deberás escribir: 4 6 8

a = int(input("Desde qué número: "))
b = int(input("Hasta qué número: "))

if b > a:
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=" ")
else:
    for i in range(b, a+1):
        if i % 2 == 0:
            print(i, end=" ")

# Repaso para junio 51

# (Ejemplo de examen de mínimos, 3/12)

# 51.- Pide al usuario dos números enteros. Muestra los números que van 
# del menor de ellos al mayor de ellos, ambos incluidos. Por ejemplo, si 
# el usuario introduce 5 y 3, deberás escribir: 
# 
# 3 
# 4 
# 5

a = int(input("Desde qué número: "))
b = int(input("Hasta qué número: "))

if b > a:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(b, a+1):
        print(i)

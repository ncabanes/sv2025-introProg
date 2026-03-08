# Repaso para junio 08

# Haz un programa que pida al usuario dos 
# números enteros y muestre el resto de la 
# división del primero entre el segundo.

a = int(input("¿Primer número? "))
b = int(input("¿Segundo número? "))
print("La división de",
    a, "entre", b, "es", a//b)
print("El resto de dividir",
    a, "entre", b, "es", a%b)

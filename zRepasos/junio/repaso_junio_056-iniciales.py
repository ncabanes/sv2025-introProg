# Repaso para junio 56

# (Ejemplo de examen de mínimos, 8/12)

# 56.- Pide al usuario que introduzca su nombre y su apellido (en una 
# única cadena de texto), y muestra sus iniciales: la primera letra del 
# nombre en mayúsculas, un punto y la primera letra del apellido en 
# mayúsculas, seguida también por un punto. Supondremos que el nombre y 
# el apellido estarán separados por un único espacio en blanco. Por 
# ejemplo, si introduce "Bill gates", tu programa debería responder 
# "B.G.".

nombreApell = input("Dime nombre y apellido: ")
nombreApellMays = nombreApell.upper()
trozos = nombreApellMays.split()
nombre = trozos[0]
apellido = trozos[1]
print(nombre[0]+"."+apellido[0]+".")

# n = input("Dime nombre y apellido: ")
# print(n.upper().split()[0][0]+"."+
#     n.upper().split()[1][0]+".")

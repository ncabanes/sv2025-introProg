# Muestra un calendario, pidiendo al usuario la cantidad de días del mes 
# (por ejemplo, 31) y el número dentro de la semana que ocupa el primer día 
# (por ejemplo, 2 para el martes). El resultado debería ser algo como:
# 
#   L   M   X   J   V   S   D
# 
#       1   2   3   4   5   6
#   7   8   9  10  11  12  13
#  14  15  16  17  18  19  20
#  21  22  23  24  25  26  27
#  28  29  30  31
# 
# Cuando tengas clara la lógica, crea una función 
# escribir_calendario(dias, dia_inicial) que contenga toda esa lógica, 
# y pruébala desde el cuerpo del programa.

# Versión 1, sin función

dias = 31
comienzo = 3
dias_escritos = 0

# Espacio inicial en la primera fila
for espacios in range(comienzo-1):
    print("   ", end="")
    dias_escritos += 1

for dia in range(1, dias+1):
    # Dos letras para los menores de 10
    if dia < 10:
        print(" ", end="")

    # El día, claro  ;-)
    print(dia, end=" ")
    dias_escritos += 1
    
    # Salto de línea cada 7 días
    if dias_escritos % 7 == 0:
        print()

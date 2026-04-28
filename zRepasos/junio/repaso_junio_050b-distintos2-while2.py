# Repaso para junio 50

# (Ejemplo de examen de mínimos, 2/12)

# 50.- Pide al usuario que introduzca dos números enteros distintos. Si 
# los que introduce no son distintos, deberás responderle "Incorrecto" y 
# volverle a pedir ambos. Esto debe repetirse hasta que realmente 
# introduzca dos números distintos, y en ese momento escribirás 
# "Correcto" y finalizará la ejecución.

# Versión 2: alternativa con "booleanos", más compacta,
# más elegante, pero más avanzada, menos fácil para principiantes

terminado = False

while not terminado:
    print("Tienes que decirme dos números distintos")
    n1 = int(input("Dime el primer número: "))
    n2 = int(input("Dime el segundo número: "))
    
    if n1 == n2:
        print("Incorrecto")
    else:
        terminado = True

print("Correcto")

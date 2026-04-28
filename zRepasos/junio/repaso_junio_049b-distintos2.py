# Repaso para junio 49

# (Ejemplo de examen de mínimos, 1/12)

# 49.- Pide al usuario que introduzca dos números enteros distintos. 
# Después de leer los números, responde "Correcto" o "Incorrecto", según 
# corresponda. Por ejemplo, si introduce 3 y 4, tu respuesta debería ser 
# "Correcto"; si introduce 6 y 6, deberías responder "Incorrecto".

# Versión 2: usando el operador "==" (igual a)

print("Tienes que decirme dos números distintos")
n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))

if n1 == n2:
    print("Incorrecto")
else:
    print("Correcto")

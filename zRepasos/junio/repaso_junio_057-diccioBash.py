# Repaso para junio 57

# (Ejemplo de examen de mínimos, 9/12)

# 57.- Crea un pequeño diccionario "bash-python". Tendrá al menos 5 
# traducciones (que pueden ser inventadas) de órdenes de bash a órdenes 
# de Python. El usuario podrá teclear una orden de "bash" (por ejemplo, 
# "echo") y se le responderá su equivalente en Python (por ejemplo, 
# "print"), o bien se le responderá "Orden desconocida" si ha tecleado 
# una orden que no aparece en nuestro diccionario.

diccioBashPython = {
    "echo" : "print",
    "read" : "input",
    "if"   : "if",
    "for"  : "for",
    "case" : "if-elif"
}

orden = input('Dime una orden de "bash": ')
if orden in diccioBashPython:
    print( diccioBashPython[orden] )
else:
    print("Orden desconocida")

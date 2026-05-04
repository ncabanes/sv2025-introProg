# Repaso para junio 54

# (Ejemplo de examen de mínimos, 7/12)

# 55.- Crea una función "saludarMucho", que escriba "Hola " y el nombre 
# que indiques como primer parámetro, tantas veces como indique el 
# segundo parámetro. Pruébala. Por ejemplo, si llamada es 
# "saludarMucho('Profe', 3)" debería escribir
# 
# Hola Profe
# Hola Profe
# Hola Profe

# Versión 1: sin indicar tipos de datos

def saludarMucho(nombre, veces):
    for i in range(veces):
        print("Hola", nombre)

saludarMucho("Fran", 4)

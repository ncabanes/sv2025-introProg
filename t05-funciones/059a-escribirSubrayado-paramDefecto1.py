# Ejercicio 59. Función escribir_subrayado, parámetro por defecto

# Crea una nueva versión de la función "escribir_subrayado", que reciba como 
# segundo parámetro (opcional) el símbolo a usar para subrayar. Si no se
# indica ese símbolo, se subrayará con guiones.

# Versión 1: acercamiento, todavía sin valor por defecto

def escribir_subrayado(texto : str, simbolo : str):
    print(texto)
    print(simbolo * len(texto) )

escribir_subrayado("Hola", '=')

print()
escribir_subrayado("Adios", '*')

print()
escribir_subrayado("Sebastián quiere un texto más largo", '/')

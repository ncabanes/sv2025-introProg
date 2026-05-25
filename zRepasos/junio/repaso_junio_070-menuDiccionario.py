# Repaso para junio 70

# 70.- Usando un diccionario, crea un menú para las opciones de un 
# programa. Deberá contener al menos las opciones "Añadir" (letra "A"), 
# "Mostrar" (letra "M"), "Borrar" (letra "B") y "TerminaR" (letra "R"). 
# Para probar que el diccionario está bien creado, el usuario introducirá 
# una letra y tu programa le mostrará el nombre de la opción asociada, o 
# el texto "Opción desconocida". Por ejemplo, si el usuario introduce 
# "A", le responderás "Añadir", mientras que si introduce "T" le dirás 
# "Opción desconocida".
    
opciones_menu = {
    "A": "Añadir",
    "M": "Mostrar",
    "B": "Borrar",
    "R": "TerminaR"
}

letra = input("Opción? ").upper()
if letra in opciones_menu:
    print(opciones_menu[letra])
else:
    print("Opción desconocida")

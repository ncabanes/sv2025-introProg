# Repaso para junio 17

# Pide al usuario que escriba "otorrinolaringología".
# Debe repetirlo hasta que lo haga correctamente.

respuesta = input("Escribe otorrinolaringología: ")
while respuesta != "otorrinolaringología":
    print("Vaya...")
    respuesta = input("Escribe otorrinolaringología: ")

print("¡Perfecto!")

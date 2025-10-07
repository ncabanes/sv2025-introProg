# 26. Password

# Pide al usuario una contraseña, tantas veces como 
# sea necesario, hasta que introduzca "1234".

# Versión 2 (incorrecta): "if", 3 intentos...

password = input("Password? ")

if password == "1234":
    print("Bienvenido")
else:
    print("Acceso denegado")
    password = input("Password? ")
    if password == "1234":
        print("Bienvenido")
    else:
        print("Acceso denegado")
        password = input("Password? ")
        if password == "1234":
            print("Bienvenido")
        else:
            print("Acceso denegado")
    

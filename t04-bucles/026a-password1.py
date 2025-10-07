# 26. Password

# Pide al usuario una contraseña, tantas veces como 
# sea necesario, hasta que introduzca "1234".

# Versión 1 (incorrecta): intento con "if"

password = input("Password? ")

if password == "1234":
    print("Bienvenido")
else:
    print("Acceso denegado")
    

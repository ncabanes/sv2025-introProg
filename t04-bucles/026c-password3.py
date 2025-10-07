# 26. Password

# Pide al usuario una contraseña, tantas veces como 
# sea necesario, hasta que introduzca "1234".

# Versión 3 (correcta): "while"

password = input("Password? ")

while password != "1234":
    print("Acceso denegado")
    password = input("Password? ")

print("Bienvenido")
    

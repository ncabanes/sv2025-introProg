# Login

# Crea un programa que pregunte al usuario su nombre. Si coincide 
# con el tuyo, le dirá algo como "Acceso concedido". Si no es así, 
# le responderá "No te denegado".

# Versión 2, con el operador !=

nombre = input("Login?")
if nombre != "Valentino":
    print ("Acceso denegado")
else:
    print ("Acceso concedido")

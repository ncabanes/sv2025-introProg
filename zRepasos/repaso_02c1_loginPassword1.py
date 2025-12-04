# 3. Pregunta al usuario su login y su PIN y 
# no le dejes acceder hasta que el nombre
# sea "yo" y el pin sea "1234". 

login = input("Login? ")
passwd = input("PIN? ")
while login != "yo" or passwd != "1234":
	print("Incorrect data")
	login = input("Login? ")
	passwd = input("PIN? ")

print("Welcome")

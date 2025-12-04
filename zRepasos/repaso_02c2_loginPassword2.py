# 3. Pregunta al usuario su login y su PIN y 
# no le dejes acceder hasta que el nombre
# sea "yo" y el pin sea "1234". 

accepted = False
while not accepted:
	
	login = input("Login? ")
	passwd = input("PIN? ")
	
	if login != "yo" or passwd != "1234":
		print("Incorrect data")
	else:
		accepted = True
	

print("Welcome")

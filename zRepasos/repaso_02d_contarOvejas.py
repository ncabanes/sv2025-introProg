# 4. Ayuda a dormir al usuario de tu 
# aplicación. Deberás contar tantas ovejas 
# como te indique. 

ovejas = int(input("Cuantas ovejas? "))
for i in range(1, ovejas+1):
	print(i, end="")
	if i == 1:
		print(" ovejita")
	else:
		print(" ovejitas")

# Repaso para junio 69

# 69.- Pide una frase al usuario y escríbela con mayúsculas correctas: 
# la primera letra en mayúsculas y el resto en minúsculas. Por ejemplo, 
# si introduce "buenos Dias", tu escribirás "Buenos dias". 

frase = input("Dime una frase y corregiré tus mayúsculas: ")
print( frase[0].upper() + frase[1:].lower() )

# Reto 08: Anagramas
# https://www.geeksforgeeks.org/problems/anagram-1587115620/1

"""
Dadas dos cadenas no vacías, s1 y s2, compuestas únicamente por letras 
minúsculas del alfabeto inglés, determine si son anagramas entre sí.

Dos cadenas se consideran anagramas si contienen los mismos caracteres con 
la misma frecuencia, independientemente de su orden.

Ejemplos:

Entrada: s1 = "geeks" s2 = "kseeg"
Salida: true
Explicación: Ambas cadenas contienen los mismos caracteres con la misma 
  frecuencia. Por lo tanto, son anagramas.

Entrada: s1 = "allergy", s2 = "allergyy"
Salida: false
Explicación: Aunque los caracteres son prácticamente iguales, s2 contiene 
  un carácter 'y' adicional. Dado que la frecuencia de los caracteres difiere, 
  las cadenas no son anagramas. 

Entrada: s1 = "listen", s2 = "lists"
Salida: false
Explicación: Los caracteres de las dos cadenas no son iguales; algunos 
  faltan o sobran. Por lo tanto, no son anagramas.

"""

def son_anagramas(s1, s2):
    # Si no tienen la misma longitud, no pueden ser anagramas
    if len(s1) != len(s2):
        return False

    # Convertimos a listas de caracteres
    lista1 = list(s1)
    lista2 = list(s2)

    # Ordenamos las listas
    lista1.sort()
    lista2.sort()

    # Comparamos
    return lista1 == lista2


# Programa principal
texto1 = input()
texto2 = input()

if son_anagramas(texto1, texto2):
    print("SI")
else:
    print("NO")

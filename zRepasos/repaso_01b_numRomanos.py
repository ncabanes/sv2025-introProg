# 2. Haz un programa que pida al usuario un número del 1 al 10 y lo 
# escriba en números romanos. La equivalencia es I, II, III, IV, V, VI, 
# VII, VIII. IX, X. Debe repetirse hasta que escriba el número 0 (que no 
# tiene equivalencia en números romanos).

n = input("Número (1 al 10; 0 para terminar)? ")

while n != "0":

    if n == "1":
        print("I")
    elif n == "2":
        print("II")
    elif n == "3":
        print("III")
    elif n == "4":
        print("IV")
    elif n == "5":
        print("V")
    elif n == "6":
        print("VI")
    elif n == "7":
        print("VII")
    elif n == "8":
        print("VIII")
    elif n == "9":
        print("IX")
    elif n == "10":
        print("X")
    elif n == "0":
        print("Hasta luego!")
    else:
        print("Número no válido")

    n = input("Número (1 al 10; 0 para terminar)? ")

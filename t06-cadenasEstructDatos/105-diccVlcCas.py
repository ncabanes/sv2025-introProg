# Diccionario de valenciano a castellano

diccionario = {
    "finestra" : "ventana",
    "taula" : "mesa",
    "aigua" : "agua",
    "oberta" : "abierta",
}

terminado = False
while not terminado:

    print("1- Añadir una palabra")
    print("2- Traducir una palabra")
    print("3- (Intentar) Traducir una frase")
    print("0- Salir")

    opcion = input("Qué opcion? ")
    print()

    if opcion == "1":
        print("Añadir")
        vlc = input("Dime la palabra en valenciano a añadir: ")
        cas = input("Dime la palabra en castellano: ")
        diccionario[ vlc ] = cas

    elif opcion == "2":
        print("Traducir")
        vlc = input("Dime la palabra en valenciano a traducir: ")
        if vlc in diccionario:
            print( diccionario[ vlc ]  )
        else:
            print("No conozco esa palabra")
        
    elif opcion == "3":
        print("Frase")
        frase = input("Dime la frase en valenciano a traducir: ")
        for palabra in frase.split():
            if palabra in diccionario:
                print(diccionario[palabra], end = " ")
            else:
                print(palabra, end = " ")
            
    elif opcion == "0":
        terminado = True
        print("Hasta luego")
    else:
        print("Opción no válida")

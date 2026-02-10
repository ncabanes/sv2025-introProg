# Lista de libros

"""
Vamos a crear un programa que nos permita llevar una lista de los 
libros que tenemos en casa.

De cada libro querremos almacenar el título, el autor y la ubicación.

El programa debe:

1. Mostrar un menú que recuerde al usuario todas las opciones 
disponibles y se repita hasta que se recoja la opción "T" (Terminar), 
que deberá funcionar tanto en mayúsculas como en minúsculas. (1 punto) 

2. Permitir añadir los datos de un nuevo libro, que se guardarán en un 
diccionario, que a su vez será parte de una lista llamada "libros". (2 
puntos) 

3. Ver los libros existentes. Para cada libro se mostrará su número 
(contando desde 1) y su título. (1 punto)

4. Ver detalles de un libro, a partir de su número. Si el número 
corresponde a un libro existente, se mostrará su título, autor y 
ubicación. Si el número es incorrecto, se avisara al usuario. (1 punto) 

5. Modificar un libro, a partir de su número. Si el número corresponde 
a un libro existente, se volverá a pedir su título, autor y ubicación. 
Si el número es incorrecto, se avisara al usuario. (1 punto)

6. Buscar en los libros que contienen un cierto texto como parte de su 
título o de su autor, quizá con mayúsculas distintas, y mostrarlos. 
Para cada libro que cumpla con esos criterios, se mostrará su número, 
su título y su autor (1 punto).

7. Los datos se guardarán tras cada cambio (cuando se añada un dato o 
cuando se modifique). (1 punto)

8. Los datos anteriores, si existían se cargarán al comenzar la 
ejecución del programa. (1 punto)

9. Es deseable que el programa esté dividido en funciones para 
facilitar su legibilidad y su mantenibilidad. Estas funciones no 
compartirán variables globales sino que recibirán la lista de libros 
como parámetro, y la devolverán modificada en los casos en los que sea 
necesario. (1 punto)
"""


def guardar(libros: list) -> None:
    f = open("libros.txt", "w")
    for l in libros:
        f.write(l["titulo"]+"$"+l["autor"]+"$"+l["ubicacion"]+"\n")
    f.close()

def cargar() -> list:
    libros = []
    try:
        f = open("libros.txt", "r")
        linea = f.readline().rstrip()
        while linea:
            fragmentos = linea.split("$")
            libros.append({
                "titulo" : fragmentos[0],
                "autor" : fragmentos[1],
                "ubicacion": fragmentos[2] })
            linea = f.readline().rstrip()
        f.close()
    except:
        print("No hay datos anteriores. Se creará un fichero nuevo.")
    return libros

def anadir(libros: list) -> list:
    titulo = input("Título? ")
    autor = input("Autor? ")
    ubicacion = input("Ubicación? ")
    libros.append({
        "titulo" : titulo,
        "autor" : autor,
        "ubicacion": ubicacion })
    return libros

def ver_todos(libros :list) -> None:
    for i in range(len(libros)):
        print(i+1, libros[i]["titulo"])

def ver_detalles(libros: list) -> None:
    numero = int(input("Número de libro? ")) - 1
    if numero >= 0 and numero < len(libros):
        print("Título:", libros[numero]["titulo"])
        print("Autor:", libros[numero]["autor"])
        print("Ubicación:", libros[numero]["ubicacion"])
    else:
        print("Número incorrecto")

def modificar(libros: list) -> list:
    numero = int(input("Número de libro? ")) - 1
    if numero >= 0 and numero < len(libros):
        titulo = input("Nuevo título? ")
        autor = input("Nuevo autor? ")
        ubicacion = input("Nueva ubicación? ")
        libros[numero] = {
            "titulo" : titulo,
            "autor" : autor,
            "ubicacion": ubicacion }
    else:
        print("Número incorrecto")
    return libros

def buscar(libros: list) -> None:
    texto = input("Texto a buscar? ").upper()
    for i in range(len(libros)):
            if texto in libros[i]["titulo"].upper() \
                    or texto in libros[i]["autor"].upper():
                print(i+1, libros[i]["titulo"],"-",
                    libros[i]["autor"])    

def mostrar_menu() -> None:
    print()
    print("1- Añadir un libro")
    print("2- Ver todos los libros")
    print("3- Ver detalles de un libro")
    print("4- Modificar")
    print("5- Buscar")
    print("T- Terminar")

# --------- Cuerpo del programa ------

libros = cargar()

seguir = True

while seguir:
    mostrar_menu()
    
    opcion = input("Opción? ").upper()
    if opcion == "1":
        libros = anadir(libros)
        guardar(libros)
    elif opcion == "2":
        ver_todos(libros)
    elif opcion == "3":
        ver_detalles(libros)
    elif opcion == "4":
        libros = modificar(libros)
        guardar(libros)
    elif opcion == "5":
        buscar(libros)
    elif opcion == "T":
        seguir = False
    else:
        print("Opción no válida")

print("Hasta otra!")

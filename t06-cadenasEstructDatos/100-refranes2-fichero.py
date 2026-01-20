# Cargar refranes desde fichero
try:
    with open("refranes.txt", "r", encoding="utf-8") as f:
        refranes = [line.strip() for line in f]
except FileNotFoundError:
    refranes = []

terminado = False

while not terminado:

    print("1 - Añadir un refrán")
    print("2 - Ver todos los refranes")
    print("3 - Ordenar alfabéticamente")
    print("T - Terminar")

    opcion = input().upper()

    if opcion == "1":
        refran = input("Refrán: ")
        refranes.append(refran)

    elif opcion == "2":
        for r in refranes:
            print(r)

    elif opcion == "3":
        refranes.sort()
        print("Refranes ordenados.")

    elif opcion == "T":
        terminado = True
        
# Guardar refranes en fichero
with open("refranes.txt", "w", encoding="utf-8") as f:
    for r in refranes:
        f.write(r + "\n")
print("Refranes guardados. ¡Hasta la próxima!")

# 1. Crea un programa que te pregunte una unidad de medida de longitud 
# (pulgadas, pies o yardas), una cantidad (por ejemplo, 2.4) y te diga 
# cuántos metros son, usando como equivalencias: 1 pulgada = 0.0254 m, 1 
# pie = 0.3048 m, 1 yarda = 0,9144 m. Por ejemplo, si la unidad es "pies" 
# y la cantidad es "3.2", la respuesta debería ser "0.97536 m".

unidad = input("Unidad de medida? ")
cantidad = float(input("Cantidad? "))

if unidad == "pulgadas":
    print(cantidad * 0.0254, "m")
elif unidad == "pies":
    print(cantidad * 0.3048, "m")
elif unidad == "yardas":
    print(cantidad * 0.9144, "m")
else:
    print("Unidad desconocida")

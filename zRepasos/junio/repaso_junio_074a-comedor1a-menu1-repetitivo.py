# Repaso para Junio 74 (semana del 25/05 al 31/05)
# 
# (Este ejercicio es un ejemplo de cómo podría ser el examen final 
# "grande", valorado de 0 a 10).
# 
# El servicio de comedor de un pequeño hospital te ha pedido que les 
# ayudes a apuntar los menús que van realizando, para evitar repetirse.
# 
# Para cada menú desean apuntar el nombre del primer plato (por ejemplo, 
# "crema de zanahorias"), el nombre del segundo plato (por ejemplo, "lomo 
# en salsa"), la fecha (como texto, por ejemplo, "2026-02-20") y las 
# calorías estimadas (un número sin decimales).
# 
# El programa debe:
# 
# 1. Mostrar un menú que recuerde al usuario todas las opciones 
# disponibles y se repita hasta que se escoja la opción "A" (Acabar), que 
# deberá ser aceptable tanto en mayúsculas como en minúsculas. (1 punto) 

print("1- Añadir menú")
print("2- Ver menús entre 2 fechas")
print("A- Acabar")
opcion = input("Dime una opción: ")

while opcion != "A":
    print("1- Añadir menú")
    print("2- Ver menús entre 2 fechas")
    print("A- Acabar")
    opcion = input("Dime una opción: ")

print("Hasta luego")

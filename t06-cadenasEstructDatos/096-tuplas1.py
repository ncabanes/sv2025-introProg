# Pide al usuario un número entero del 1 al 
# 12 y escribe el nombre del mes correspondiente
# (1=enero, 12=diciembre), usando una tupla para 
# almacenar los nombres.

meses = ("enero", "febrero", "marzo", 
    "abril", "mayo", "junio")

numero_mes = int(input("Dime el número de mes: "))
print(meses[numero_mes-1])

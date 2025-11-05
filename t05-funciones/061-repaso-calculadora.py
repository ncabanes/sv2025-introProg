# 61. Crea un programa que pida un número entero, un operador (+ - * o /) y otro 
# número entero y muestre el resultado de esa operación. Por ejemplo:
# 
# Numero? 5
# Operacion? +
# Numero? 3
# 5+3=8

n1 = int(input("Numero?"))
simbolo = input("Operacion?")
n2 = int(input("Numero?"))

if simbolo == "+":
    print(n1, simbolo, n2, "=", n1 + n2)
elif simbolo == "-":
    print(n1, simbolo, n2, "=", n1 - n2)
elif simbolo == "*":
    print(n1, simbolo, n2, "=", n1 * n2)
elif simbolo == "/":
    print(n1, simbolo, n2, "=", n1 / n2)
else:
    print("operacion incorrecta")

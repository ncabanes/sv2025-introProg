# Haz un programa que calcule una aproximación para PI, usando la expresión 
# pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 ...  El usuario indicará 
# cuántos términos se deben usar (por ejemplo, si responde que 2, tu programa 
# calcularía 1/1 - 1/3, que tendrá como resultado algo cercano a 0.666666, luego 
# el valor aproximado de PI (con 2 sumandos) sería 4 * 0.666666 = 2.666666). 
# Nota: Este método se llama "fórmula de Leibniz": 
# https://es.wikipedia.org/wiki/Serie_de_Leibniz

# Cuando tengas clara la lógica, crea una función aproximar_pi_leibniz(terminos) 
# que contenga toda esa lógica y que devuelva el valor aproximado de pi para esa 
# cantidad de términos, y pruébala desde el cuerpo del programa.

# Versión 1, sin función

denominador = 1
signo = 1
terminos = 2

pi_entre_cuatro = 0

for i in range(terminos):
    pi_entre_cuatro += signo * 1 / denominador
    signo *= -1
    denominador += 2

print(4 * pi_entre_cuatro)

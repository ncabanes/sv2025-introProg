# Crea una lista con los nombres de los días de la semana. Luego muestra el 
# nombre del segundo día, los nombres de todos ellos (de principio a fin) y 
# los nombres en orden inverso (de último a primero).

dias = ["lunes", "martes", "miércoles", "jueves",
        "viernes", "sábado", "domingo"]

# Segundo día
print(dias[1])

# Todos en orden
for dia in dias:
    print(dia)

# Todos, del último al primero
for i in range(len(dias)-1, -1, -1):
    print(dias[i])

# Mostrar todos, rápido y cutre
print(dias)

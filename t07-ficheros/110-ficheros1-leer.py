fich = open("multiplosDe7.txt", "w") 

for i in range(1,101):
    if i % 7 == 0:
       fich.write(str(i) + "\n") 

fich.close()

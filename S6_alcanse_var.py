def contar():
    cont = 0  #variable local de la funcion contar
    cont = cont + 1 # suma 1 a la variable local cont
    print(" VAR cont de la funcion: ", cont)

cont = 100  # declara variable local de main
cont= cont + 1 #suamndo 1 a la variable local de main
contar()
contar()
contar()
print(" VAR cont de main: ", cont)
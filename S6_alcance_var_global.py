cont = 0 # global

def contar():
    global cont # llamar a la variable devlarada como global
    cont = cont + 1 # suma 1 a la variable global cont
    print(" Valorde cont desde la funcion: ", cont)

if __name__ == "__main__":
    print("valor de cont: ", cont)
    contar()
    contar()
    contar()
    print(" valor de cont: ", cont)
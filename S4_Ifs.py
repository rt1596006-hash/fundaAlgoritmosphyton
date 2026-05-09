nota = float(input("ingrese nota: "))
if nota <= 20 and nota >= 0:
    if nota >= 17 :
        print ("excelente")
    elif nota >= 11:
        print("aprobado")
    else:
        print("desaprobado")
else:
    print("nota invalida")
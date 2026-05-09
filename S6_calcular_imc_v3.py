def calcularimc(peso,altura):
    imc = 0.0
    # validar datos de entrada
    valido = validarentrada(peso, altura)
    if valido == True:
        #proceso
        imc = peso / altura ** 2
    else:
        print("datos de entrada no validos")
    return imc

def validarentrada(peso, altura):
    valido = False
    if peso <= 400 and peso >=5:
        if altura <= 2.5 and altura >= 0.6:
            valido = True
        else:
            print("altura no valida")
            valido = False
    else:
        print("peso no valido")
        valido = False
    return valido
# programa que calcula el imc
# declaracion y obtencion de datos
peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros: "))
imc = calcularimc(peso, altura)
if imc > 0 :
    #mostar informacion
    print("su imc es: ", imc)
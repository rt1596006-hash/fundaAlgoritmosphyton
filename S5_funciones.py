import math
#palabra reservada def nombre de funcion(parametros)
def areacirculo(radio):
    # proceso
    resultado = math.pi * (radio) ** 2
    #retornar el resultado al usuario
    return resultado

# obtener el valor del radio del usuario
radio = float(input("ingrese radio del circulo:  "))
# invocar a la funcion para calcular el valor de area del circulo
resultado = areacirculo(radio)
print(" el valor del area del circulo es: ", resultado)

##obtener el area del triangulo
def areatriangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

base = float(input("ingrese la base del triangulo: "))
altura = float(input("ingrese la altura del triangulo: "))
if base > 0 and altura > 0:
    resultado = areatriangulo(base, altura)
    print(" el valor del area del triangulo es: ", resultado)
else:
    print("existe un error en los valores ingresados")
print("fin del programa")
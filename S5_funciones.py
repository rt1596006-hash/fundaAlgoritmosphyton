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


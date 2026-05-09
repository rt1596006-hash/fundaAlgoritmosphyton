print("###### menu malculadora ####")
print("menu operaciones")
print("1.suma")
print("1.resta")
print("1.multiplicacion")
print("1.division")
print("1")
resultado = 0.0
a = float(input("ingresa primer numero"))
b = float(input("ingresa segundo numero"))
opc = float(input("ingresa opocion"))
match opc:
    case 1:
        resultado = a+b
    case 2:
        resultado = a-b
    case 3:
        resultado = a*b
    case 4:
        resultado = a/b
print("resultado" , resultado)
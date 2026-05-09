valores = [84, 12 ,57, 93, 2, 45,68,19,71,33,5,88,14,62,27,99,41,7,
                    50,76,18,91,24,66,3,54,82,39,11,73,48,8,95,21,60,36,1,79,
                    44,15,87,52,6,92,30,64,23,77,49,10];
print ("valores almacenados")
for i in range(len(valores)):
    print(valores[i], ", ")

#captura de datos del usuario
valorbuscar = int(input("ingrese el valor a buscar: "))

#busqueda lineal
pos = -1
for i in range(len(valores)):
    if valores[i] == valorbuscar:
        pos = i
        break

if pos == -1:
    print("valor no encontrado")
else:
    print("valor encontrado en la posicion: ", pos)
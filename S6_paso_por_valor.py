
precio = 100.50
preciocondescuento = 0.0
def calculardescuento(_precio):
    if _precio > 80:
        _precio = _precio - (_precio * 0.10) #aplica un descuento del 10% al precio
    print("precio original: ", precio)
    return _precio

print("precio original: ", precio)
preciocondescuento = calculardescuento(precio)
print("precio con descuento: ", preciocondescuento)
#*********** ZONA DE FUNCIONES ************#
def pedir_valor():
    precio = float(input("Ingrese el valor del producto: "))
    return precio


def pedir_cantidad():
    cantidad = int(input("Ingrese la cantidad: "))
    return cantidad


def calcular_datos():
    subtotal = 0
    reanudar = input("¿Desea agregar un producto? (Si / No): ")
    while reanudar != "No":
        precio = pedir_valor()
        cantidad = pedir_cantidad()
        subtotal = subtotal + (precio * cantidad)
        reanudar = input("¿Desea agregar un producto? (Si / No): ")
    return subtotal


def calcular_descuento(subtotal):
    if subtotal > 1000:
        descuento = subtotal * 0.10
        
    else:
        if subtotal > 500:
            descuento = subtotal * 0.05
            
        else:
            descuento = 0
    total = subtotal - descuento
    return total, descuento


def Imprimir_resultado(total, descuento):
    print("El descuento es: ", descuento)
    print("Valor total a pagar: ", total)


#*********** CODIGO PRINCIPAL DE PYTHON ************#
subtotal = calcular_datos()
total, descuento = calcular_descuento(subtotal)
Imprimir_resultado(total, descuento)
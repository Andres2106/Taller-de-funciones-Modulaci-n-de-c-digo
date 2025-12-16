#*********** ZONA DE FUNCIONES ************#
def pedir_venta():
    ventas = float(input("Ingrese el monto de la venta: "))
    return ventas


def calcular_venta():
    meta = 5000
    cumplido = 0
    total = 0
    venta = pedir_venta()
    while venta > 0:
        total = total + 1
        if venta >= meta:
            cumplido = cumplido + 1
            print("META COMPLETADA!")
        else:
            print("Meta NO cumplida.")
        venta = pedir_venta()
        if venta <= 0:
            break
    return cumplido, total


def Imprimir_resultado(cumplido, total):
    print("Total vendedores que cumplieron: ", cumplido)
    print("Total vendedores procesados: ", total)


#*********** CODIGO PRINCIPAL DE PYTHON ************#
cumplido, total = calcular_venta()
Imprimir_resultado(cumplido, total)
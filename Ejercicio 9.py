#*********** ZONA DE FUNCIONES ************#
def pedir_cantidad_vendido():
    vendido = int(input("Ingrese la cantidad vendida: "))
    return vendido

def Calcular_inventario():
    stock = 50
    punto = 10
    vendido = pedir_cantidad_vendido()
    
    while vendido >= 0:
        
        stock = stock - vendido

        if stock <= punto:
            print("Aviso de Reposición Urgente.")
            break

        vendido = pedir_cantidad_vendido()

    return stock

def Imprimir_inventario(stock):
    print("Resultado stock final:", stock)
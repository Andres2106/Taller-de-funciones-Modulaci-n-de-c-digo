#*************** ZONA DE FUNCIONES ***************#
def pedir_producto():
    producto = int(input("Ingrese el número del producto (1, 2  o 3): "))
    return producto


def cantidad():
    cantidad = int(input("Ingrese la cantidad de productos: "))
    return cantidad


def procesar_informacion(calificacion):
    total = 0
    contador = 0   
    for n in range(calificacion):
        print("Califica tu pedido")
        calificacion = int(input("del 1 al 5: "))  
        if calificacion > 5:
            calificacion = 5
        if calificacion < 1:
            calificacion = 1
        if calificacion == 5:
            print("Excelente!")  
        total = total + calificacion
        contador = contador + 1
    return total, contador


def calcular(total, contador):
    if contador > 0:
        promedio = total / contador
    else:
        promedio = 0
    return promedio


def mostrar(promedio):
    print("El promedio es:", promedio)


#*************** CÓDIGO PRINCIPAL DE PYTHON ***************#
producto = pedir_producto()
cantidad = cantidad()
total, contador = procesar_informacion(cantidad)
promedio = calcular(total, contador)
mostrar(promedio)
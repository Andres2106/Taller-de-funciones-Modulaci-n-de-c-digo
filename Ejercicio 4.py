#*********** ZONA DE FUNCIONES ************#
def pedir_unidad():
    unidad = int(input("Ingrese la cantidad de unidades: "))
    return unidad


def pedir_estado():
    estado = input("Ingrese el estado (D defectuoso, B Buen estado): ")
    return estado


def calcular_datos():
    defectuoso = 0
    buen_estado = 0
    reanudar = input("Escriba F para finalizar o C para continuar: ")
    
    while reanudar != "F":
        Unidad = pedir_unidad()

        contador = 0
        while contador < Unidad:
            estado = pedir_estado()

            if estado == "D":
                defectuoso = defectuoso + 1
                
            else:
                if estado == "B":
                    buen_estado = buen_estado + 1
                    
                else:
                    print("Estado no válido.")
                    contador = contador - 1
                    
            contador = contador + 1
    
        reanudar = input("Escriba F para finalizar o C para continuar: ")
    
    return defectuoso, buen_estado

def Imprimir_resultado(defectuoso, buen_estado):
    total = defectuoso + buen_estado
    
    if total > 0:
        porcentaje = (defectuoso * 100) / total
    else:
        porcentaje = 0

    print("Total de defectuosos: ", defectuoso)
    print("Total de buen estado: ", buen_estado)
    print("Porcentaje de defectuosos:  ", porcentaje)
    
    
#*********** CODIGO PRINCIPAL DE PYTHON ************#
defectuoso, buen_estado = calcular_datos()
Imprimir_resultado(defectuoso, buen_estado)
#*********** ZONA DE FUNCIONES ************#
def pedir_cpu():
    cpu = int(input("Ingrese el uso de la CPU: "))
    return cpu


def calcular_cpu():
    alerta = 0
    medicion = 0
    uso_cpu = pedir_cpu()
    while uso_cpu >= 0:
        medicion = medicion + 1
        if uso_cpu > 90:
            print("ADVERTENCIA! Uso crítico de CPU")
            alerta = alerta + 1
    return alerta, medicion


def Imprimir_resultado(alerta, medicion):
    print("Total de Medición: ", medicion)
    print("Total alerta crítica: ", alerta)


#*********** CODIGO PRINCIPAL DE PYTHON ************#
alerta, medicion = calcular_cpu()
Imprimir_resultado(alerta, medicion)
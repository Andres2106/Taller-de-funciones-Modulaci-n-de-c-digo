#*********** ZONA DE FUNCIONES ************#
def pedir_horas():
    hora = int(input("Ingrese las horas extra trabajadas: "))
    return hora
def procesar_horas():
    Total = 0
    Emp = 0
    horas = pedir_horas()
    while horas >= 0:
        if horas > 5:
            Bono = horas * 15
            Total = Total + Bono
            Emp = Emp + 1
        
        if horas > 0:
                Bono = horas * 10
                Total = Total + Bono
                emp = emp + 1
        horas = pedir_horas()
        if horas <= 0:
            break
    return Total, Emp
        
def Imprimir_resultado(Total, Emp):
    print("Total de bonificación: ", Total)
    print("Total de empleados bonificados:", Emp)


#*********** CODIGO PRINCIPAL DE PYTHON ************#
Total, Emp = procesar_horas()
Imprimir_resultado(Total, Emp)
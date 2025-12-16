#*************** ZONA DE FUNCIONES ***************#
def pedir_opcion():
 opcion = input("Seleccione (D depósito R retiro o FIN finalizar): ")
 return opcion


def Monto():
    monto = float(input("Ingrese el monto: "))
    return monto


def calcular_informacion():
    Saldo_inicial = 1000
    transaccion = 0
    Tipo = pedir_opcion()
    while Tipo != "FIN":
        if Tipo == "D":
            monto = Monto()
            Saldo_inicial = Saldo_inicial + monto
            transaccion = transaccion + 1
        else:
            if Tipo == "R":
                monto = monto()
                if Saldo_inicial - monto >= 0:
                    Saldo_inicial = Saldo_inicial - monto
                    transaccion = transaccion + 1
                else:
                    print("Error! Saldo insuficiente.")
            else:
             print("Tipo no válido.")
        Tipo = pedir_opcion()
    return saldo, transaccion


def Imprimir_resultado(saldo, transaccion):
    print("Total de saldo:", saldo)
    print("Total de transacciones válidas:", transaccion)


#*************** CÓDIGO PRINCIPAL DE PYTHON ***************#
saldo, transaccion = calcular_informacion()
Imprimir_resultado(saldo, transaccion)
#*************** ZONA DE FUNCIONES ***************#
def pedir_cod():
    cod = input("Ingrese su código: ")
    return cod
def Confirmar_codigo(cod, codigo_esp):
    if cod == codigo_esp:
        return True
    else:
        return False
def desarrollar_accesos():
    codigo_esp = "1234"
    permitido = 0
    denegado = 0
    while True:
        cod = pedir_cod()
        if cod == "Salir.":
            break
        if Confirmar_codigo(cod, codigo_esp):
            print("Accceso Permitido")
            permitido = permitido + 1
        else:
            print("Acceso denegado.")
            denegado = denegado + 1
    return permitido, denegado
        
def Imprimir_resultado(permitido, denegado):
    print("Acceso Permitido.", permitido)
    print("Acceso Denegado.", denegado)


#*************** CÓDIGO PRINCIPAL DE PYTHON ***************#
permitido, denegado = desarrollar_accesos()
Imprimir_resultado(permitido, denegado)
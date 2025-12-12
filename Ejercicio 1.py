#************* ZONA DE FUNCIONES ***************#
def definir_informacion():
    cantidad = 0
    sum_valoraciones = 0
    Excelente = 0
    

    cantidad = int(input("Ingrese la cantidad de productos: "))
    
    for i in range(cantidad):
        valoracion = int(input("Califique su producto del 1 al 5: "))
        
        while valoracion < 1 or valoracion >= 6:
            print("Error en valoración.")
            valoracion = int(input("Califique su producto del 1 al 5: "))
    
        sum_valoraciones = sum_valoraciones + valoracion
        
        if valoracion == 5:
            Excelente = Excelente + 1
            
        
        informacion = (cantidad, sum_valoraciones, Excelente)  
        return informacion
    
def Imprimir_resultado(informacion):
    cantidad, sum_valoraciones, Excelente = informacion
    
    print("Total de productos: ", str(cantidad))
    print("Valoración total: ", str(sum_valoraciones))
    print("Total de Excelentes: ", str(Excelente))
    
    
#************* ZONA DE FUNCIONES ***************#
informacion = definir_informacion()
Imprimir_resultado(informacion)
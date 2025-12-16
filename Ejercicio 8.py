#*********** ZONA DE FUNCIONES ************#
def pedir_edad():
    edad = int(input("Ingrese la edad del participante: "))
    return edad

def Calcular_edad():
    publico = 0
    sum_edad = 0
    total_p = 0

    edad = pedir_edad()
    
    while edad != 0:
        total_p = total_p + 1
        sum_edad = sum_edad + edad


        if edad >= 25 and edad <= 45:
            publico = publico + 1
            print("Ha sido registrado.")

        edad = pedir_edad()
        
        return publico, sum_edad, total_p 


def Imprimir_edades(publico, sum_edad, total_p):
    if total_p > 0:
        promedio = sum_edad / total_p
    else:
        promedio = 0

    print("Total de público objetivo:", publico)
    print("Edad promedio:", promedio)
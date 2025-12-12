#************* ZONA DE FUNCIONES ***************#
class CuentaBanco:
    
    def __init__(self, saldo_inicio):
        
        if saldo_inicio < 0:
            raise ValueError("❌ Error! el saldo inicial es negativo.")
        self.__saldo = saldo_inicio
        self.__total_transaccion_efectiva = 0
        
        
    def ingresar_deposito(self, dinero):
        
        if dinero <= 0:
            print("Error, el dinero a depositar debe ser positivo.")
            return False
        
        self.__saldo += dinero
        self.__total_transaccion_efectiva += 1
        print(f" Depósito de {dinero:.2f} realizado con éxito. ✅")
        
        return True
    
    
    def ingresar_retiro(self, dinero):
         
        if dinero <= 0:
            return False
        
        if self.__saldo - dinero >= 0:
            self.__saldo -= dinero
            self.__total_transaccion_efectiva += 1
            
            print(f"Retiro de {dinero:.2f} realizado con éxito. ✅")
            return True
        
        else:
            print(f"❌ Error de retiro! Saldo insuficiente! Saldo actual: {self.__saldo:.2f}")
            return False
    
    
    
    def imprimir_saldo(self):
        return self.__saldo
    
    
    
    def imprimir_total_transaccion(self):
        return self.__total_transaccion_efectiva
        
        
        
    def __str__(self):
        
        return (f"\n--- Información de la Cuenta ---\n"
                
                f"Saldo: {self.imprimir_saldo():.2f}\n"
                
                f"Transacciones efectivas: {self.imprimir_total_transaccion()} ✅")
    
    
def definir_informacion():
    SALDO_INICIO = 500.0
        
    print("--- INFORMACIÓN DE LA CUENTA ---")
    print(f"Saldo Inicial: {SALDO_INICIO:.2f}")
    cuenta = CuentaBanco(SALDO_INICIO)
    
    while True:
        Opcion_elegida = input("Digíte la opción que necesita ('D' depósitar, 'R' retirar, 'F' para finalizar): ").upper()

        if Opcion_elegida == "F":
            print("Proceso finalizado con éxito. ✅")
            break

        if  Opcion_elegida not in ['D', 'R']:
            print("❌ Error! Intente de nuevo.")
            continue

        try:
            dinero = float(input("Digíte el dinero: "))
        except ValueError:
            print("❌ Error! Debe ingresar solo números.")
            continue

        if  Opcion_elegida == 'D':
            cuenta.ingresar_deposito(dinero)
        elif  Opcion_elegida == 'R':
            cuenta.ingresar_retiro(dinero)
            
    print(cuenta) 
    print("------------------------------")
    
#************* ZONA DE FUNCIONES ***************#
if __name__ == "__main__":
    definir_informacion()
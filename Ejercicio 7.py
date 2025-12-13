#************* ZONA DE FUNCIONES ***************#
class Ventas:
    def __init__(self, meta_fija):
        self.__meta = meta_fija
        self.__vendedores_meta = 0
        self.__total_vendedores = 0
        self.__felicitaciones = []
    
    def definir_ventas(self, dinero_venta):
        self.__total_vendedores +=  1
        vendedor = f"Vendedor #{self.__total_vendedores}"
        
        if dinero_venta >= self.__meta:
            self.__vendedores_meta += 1
            felicitaciones = f"🎉🎖️ Felicitaciones {vendedor}! Superó la meta con: {dinero_venta} 🎖️ 🎉"
            self.__felicitaciones.append(felicitaciones)
            print(f"🎉 🎖️ META LOGRADA! 🎖️ 🎉: {dinero_venta:.2f}")
        else:
            print(f"Meta NO cumplida: {dinero_venta:.2f} 🙁")
            
        return True
    
    
    def obtener_meta_cumplida(self):
        return self.__vendedores_meta
    
    
    def obtener_vendedores(self):
        return self.__total_vendedores
    
    
    def obtener_felicitaciones(self):
        return self.__felicitaciones
    
    
    def __str__(self):
        return (f"\n------ ✨ Resultado de Metas ✨ ------\n"
                
                f"📌. Meta Mensual: ${self.__meta:.2f}\n"
                
                f"📌. Vendedores Ingresados: {self.obtener_vendedores()}\n"
                
                f"📌. Vendedores que Cumplieron: {self.obtener_meta_cumplida()}\n ✅")
        
#************* CÓDIGO PRINCIPAL DE PYTHON ***************#
def definir_informacion():
    META_FIJA = 10000
    
    print("------ ✨ META DE VENTAS ✨ ------")
    print(f"📌. La meta fija del mes es: 🏆{META_FIJA:.2f}🏆")
    
    venta = Ventas(META_FIJA)
    
    while True:
        
        try: 
            dinero = float(input("📍. Digite el dinero de las ventas del vendedor❗(Digite 0 para finalizar)❗: "))
        except ValueError:
            print("❗Error❌ Debe digitar solo números❗")
            continue
        if dinero <= 0:
            print("Programa Finalizado.")
            break
        
        venta.definir_ventas(dinero)
        
    print(venta)
    
    felicitacion = venta.obtener_felicitaciones()
    
    if felicitacion:
            
        print("------ 🎉 FELICITACIONES 🎉 ------")
        for mensaje in felicitacion:
            print (mensaje)
        print("----------------------------")
    
    else: 
        print("------ 🙁 Ningún vendedor cumplió la meta, no hay felicitaciones. 🙁 ------")

if __name__ == "__main__":
    definir_informacion()
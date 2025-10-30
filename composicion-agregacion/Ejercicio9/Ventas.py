from Orden import orden

class ventas:
    def __init__(self, no):
        self.__no = no
        self.__O=[] # Arreglo de ordenes
    
    def agregarOrden(self, nO):
        self.__O.append(nO)
    
    def getPedidosEnFechaX(self, fecha):
        for orden in self.__O:
            if(orden.getFecha() == fecha):
                print(orden)
                
    def ordenarOrdenes(self):
        for i in range(len(self.__O)-1):
            for j in range(i+1, len(self.__O)):
                if(self.__O[i].total() < self.__O[j].total()):
                    obj = self.__O[i]
                    self.__O[i] = self.__O[j]
                    self.__O[j] = obj
        
    def mostrarOrdenes(self):
        for ord in self.__O:
            print(ord)
            print("---------------------")
            print(f"total: {ord.total()}")
    
    def eliminarOrden(self, ciCli):
        for i in range(len(self.__O)):
            if(ciCli == self.__O[i].getCiCliente()):
                self.__O.pop(i)
                break
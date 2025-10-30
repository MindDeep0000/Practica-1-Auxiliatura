from Plato import plato
from multimethod import multimethod
class pedido:
    def __init__(self, nroPedido, np):
        self.__nroPedido = nroPedido
        self.__np = np
        self.__P=[] # arreglo de platos
    
    def __str__(self):
        
        return f"pedido= [nro: {self.__nroPedido} np: {self.__np} platos=[{self.getPlatos()}]]"
    
    @multimethod
    def agregarPlato(self, Nplato: plato) -> None:
        if(isinstance(Nplato, plato)):
            self.__P.append(Nplato)
            
    @multimethod
    def agregarPlato(self, platos: list[plato]) -> None:
        for o in platos:
            self.__P.append(o)
    
    def getPlatos(self):
        info ="\n"
        for a in self.__P:
            info+=a.__str__()
            info+="\n"
        return info
    
    def precioTotal(self):
        total=0
        for plato in self.__P:
            total+=plato.getPrecio()
        return total
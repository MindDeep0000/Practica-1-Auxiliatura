from Pedido import pedido
from Cliente import cliente
class orden:
    def __init__(self, fecha, hora, nroPedido, np, nomCli, apeCli, ciCli):
        self.__fecha = fecha
        self.__hora = hora
        self.__P = pedido(nroPedido, np)
        self.__C = cliente(nomCli, apeCli, ciCli)
        
    def getFecha(self):
        return self.__fecha
    
    def getPedido(self):
        return pedido
    
    def agregarPlatos(self, A_platos):
        self.__P.agregarPlato(A_platos)
    
    def __str__(self):
        return f"{self.__P}"
    
    def total(self):
        sumaTotal = self.__P.precioTotal()
        return sumaTotal

    def getCiCliente(self):
        return self.__C.getci()
from multimethod import multimethod
from Ropa import Ropa

class Ropero:
    def __init__(self, material, ropa):
        self.__material = material
        self.__Ropa = ropa
        self.__nroRopas = len(ropa)
    
    @multimethod
    def eliminarPrendas(self, material: str) -> None:
        for R in self.__Ropa:
            if(isinstance(R, Ropa)):
                if(material in R.getMaterial()):
                    self.__Ropa.remove(R)
            else:
                print("Objeto no compatible")
    
    @multimethod
    def eliminarPrendas(self, tipo: str, A: None) -> None:
        for R in self.__Ropa:
            if(isinstance(R, Ropa)):
                if(tipo in R.getTipo()):
                    self.__Ropa.remove(R)
            else:
                print("Objeto no compatible")
    
    def mostrarPrendas(self, material, tipo):
        
        for R in self.__Ropa:
            if(isinstance(R, Ropa)):
                if(tipo in R.getTipo()):
                    print(R)
                    break
                if(material in R.getMaterial()):
                    print(R)
                    break
            else:
                print("Objeto no compatible")
    
    def agregarRopa(self, ropa):
        self.__Ropa.append(ropa)
        
    def mostrarRopero(self):
        print("***************************")
        print("Ropas en el ropero")
        print("************************************************************************************************************")
        for ropa in self.__Ropa:
            if(isinstance(ropa, Ropa)):
                print(ropa)
        print("************************************************************************************************************")
from Ram import Ram
from DiscoDuro import DiscoDuro


from multimethod import multimethod
class Computadora:
    def __init__(self, año=None, ram=None, discoDuro=None):
        self.__añoEnsamblaje = año
        self.__rams=ram
        self.__discos=discoDuro
    
    def encender(self):
        print("Encendiendo la computadora, por su seguridad mantengala enchufada")
    
    def mostrar(self):
        print(f"año de ensamblaje {self.__añoEnsamblaje}")
        if(self.__rams != None):
            print(self.__rams)
        
        if(self.__discos != None):
            print(self.__discos)
    
    @multimethod
    def modificarCapacidad(self, ncap: float) -> None:
        if(isinstance(self.__rams, Ram)):
            
            if(self.validarRam()):
                self.__rams.setCapacidad(ncap)
            else:
                print("Capacidad de RAM sobrepasada NO ES POSIBLE MODIFICAR A MAS")
        else:
            print("No es posible realizar la operacion es dañina")
    @multimethod
    def modificarCapacidad(self, ncap: int) -> None:
        if(self.__discos != None):
            self.__discos.setCapacidad(ncap)
        else:
            print("Error fatal no es posible modificar el disco duro")
        
    def validarRam(self):
        if(isinstance(self.__rams, Ram)):
            cRam = self.__rams.getCapacidad()
            if(cRam >=4 and cRam <= 64):
                return True
            else:
                return False
        
        return False
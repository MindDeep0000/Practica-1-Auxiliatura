from Bateria import bateria

class celular:
    def __init__(self, marca=None, modelo=None, amp=None, material=None):
        self.__marca = marca
        self.__modelo = modelo
        self.pila = bateria(amp, material)
    
    def __str__(self):
        return f"marca: {self.__marca} modelo: {self.__modelo} {self.pila}"
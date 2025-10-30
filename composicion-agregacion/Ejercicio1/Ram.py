class Ram:
    def __init__(self, cap, marca, tipo):
        self.__capacidad = cap
        self.__marca = marca
        self.__tipo = tipo
    
    def __str__(self):
        return f"Ram [capacidad: {self.__capacidad} GB marca: {self.__marca} tipo: {self.__tipo}]"
    
    def setCapacidad(self, nCap):
        self.__capacidad = nCap
    
    def getCapacidad(self):
        return self.__capacidad
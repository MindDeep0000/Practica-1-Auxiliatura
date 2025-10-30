class DiscoDuro:
    def __init__(self, cap, marca, modelo):
        self.__capacidad = cap
        self.__marca = marca
        self.__modelo = modelo
    
    def __str__(self):
        return f"Disco [capacidad: {self.__capacidad} GB marca: {self.__marca} modelo: {self.__modelo}]"
    
    def setCapacidad(self, nCap):
        self.__capacidad = nCap
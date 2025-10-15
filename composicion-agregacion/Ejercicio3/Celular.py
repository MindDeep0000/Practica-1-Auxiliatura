class celular:
    def __init__(self, marca=None, modelo=None, Bateria=None):
        self.__marca = marca
        self.__modelo = modelo
        self.bateria = Bateria
    
    def __str__(self):
        return f"marca: {self.__marca} modelo: {self.__modelo} {self.bateria}"
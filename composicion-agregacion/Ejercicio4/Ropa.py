class Ropa:
    def __init__(self, tipo, material):
        self.__tipo = tipo
        self.__material = material

    def getMaterial(self):
        return self.__material
    
    def getTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f"tipo: {self.__tipo} Material: {self.__material}"
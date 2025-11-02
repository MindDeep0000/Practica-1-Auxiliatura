class Facultad:
    def __init__(self, nombre, nroCarreras):
        self.__nombre = nombre
        self.__nroCarreras= nroCarreras
    
    def getNombre(self):
        return self.__nombre
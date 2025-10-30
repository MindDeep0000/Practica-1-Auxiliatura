class cliente:
    def __init__(self, nombre, apellido, ci):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ci = ci
    
    def getci(self):
        return self.__ci
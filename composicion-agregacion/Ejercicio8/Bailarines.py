class Bailarin:
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
    
    def __str__(self):
        return f"{self.__nombre} {self.__edad} {self.__sexo}"
    
    def getEdad(self):
        return self.__edad
    
    def getNombre(self):
        return self.__nombre
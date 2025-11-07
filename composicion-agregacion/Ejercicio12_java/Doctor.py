class Doctor:
    def __init__(self, nom, esp):
        self.__nombre = nom
        self.__especialidad = esp
    
    def __str__(self):
        return f"nombre: {self.__nombre} esp: {self.__especialidad}"
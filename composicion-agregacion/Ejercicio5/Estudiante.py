from Persona import persona

class estudiante(persona):
    def __init__(self, nombre, paterno, materno, ci, edad, ru, matricula):
        self.__ru = ru
        self.__matricula = matricula
        super().__init__(nombre, paterno, materno, ci, edad)
    
    def getMatricula(self):
        return self.__matricula
    def __str__(self):
        return f"{super().__str__()} {self.__ru} {self.__matricula}"
    
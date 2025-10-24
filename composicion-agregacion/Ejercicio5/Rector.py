from Persona import persona

class rector(persona):
    def __init__(self, nombre, paterno, materno, ci, edad, aniosExp, sueldo):
        self.__aniosExp = aniosExp
        self.__sueldo = sueldo
        super().__init__(nombre, paterno, materno, ci, edad)
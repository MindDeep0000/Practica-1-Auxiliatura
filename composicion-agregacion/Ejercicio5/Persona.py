class persona:
    def __init__(self, nombre, paterno, materno, ci, edad):
        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._ci = ci
        self._edad = edad
    
    def getNombre(self):
        return self._nombre
    
    def getci(self):
        return self._ci
    
    def getedad(self):
        return self._edad
    
    def __str__(self):
        return f"{self.getNombre()} {self.getci()} {self.getedad()}"
    
class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
    def getSalario(self):
        return self.__sueldo
    
    def setSalario(self, nv):
        self.__sueldo = nv
    
    def getCargo(self):
        return self.__cargo
    
    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"nombre: {self.getNombre()} cargo: {self.getCargo()} sueldo: {self.getSalario()}"
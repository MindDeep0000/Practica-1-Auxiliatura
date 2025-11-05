class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"nombre: {self.__nombre} puesto: {self.__puesto} salario: {self.__salario}"
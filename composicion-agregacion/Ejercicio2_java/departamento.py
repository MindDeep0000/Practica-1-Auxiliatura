from empleado import Empleado
class Departamento:
    def __init__(self, nombre, area):
        self.__nombre = nombre
        self.__area = area
        self.__listaEmpleados = []
    def mostrarEmpleados(self):
        for N in self.__listaEmpleados:
            if(N!=None):
                print(N)
    
    def cambioSalario(self, nombre, nvsalario):
        for emp in self.__listaEmpleados:
            if(emp.getNombre() == nombre):
                print("El emplaedo: ")
                print(emp)
                print("esta cambiando su sueldo a: ")
                emp.setSalario(nvsalario)
                print(emp)
                break
    
    def añadir(self, Empleado):
        self.__listaEmpleados.append(Empleado)
    
    def eliminar(self, empleado):
        self.__listaEmpleados.remove(empleado)
        
    # def __str__(self):
    #     return f"nombre: {self.__nombre}"
    
    def getListaEmps(self):
        return self.__listaEmpleados
    
    def verificarMismoDepartamento(self, dep):
        lista = []
        lista = dep.getListaEmps()
        for A in self.__listaEmpleados:
            for B in lista:
                if(A is B):
                    print("coincidencia encontrada con: ")
                    print(A)
                    self.__listaEmpleados.remove(A)
                    break
    def cambiarDepartamento(self, dep):
        lista = self.getListaEmps()
        for valor in lista:
            dep.añadir(valor)
            self.eliminar(valor)
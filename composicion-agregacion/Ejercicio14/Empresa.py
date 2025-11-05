from Empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__empleados = []
    
    def addEmpleado(self, emp):
        self.__empleados.append(emp)
    
    def infoEmpresa(self):
        print(f"<<{self.__nombre}>>")
        for K in self.__empleados:
            print(K)
    
    def buscarEmp(self, nombre):
        for A in self.__empleados:
            if(isinstance(A, Empleado)):
                if(nombre in A.getNombre()):
                    print(A)
                    break
    
    def eliminarEmp(self, nombre):
        for A in self.__empleados:
            if(isinstance(A, Empleado)):
                if(nombre in A.getNombre()):
                    print("eliminar empleado")
                    print(f"*** {A} ***")
                    self.__empleados.remove(A)
                    break
    
    def promedioSalarios(self):
        Temp = len(self.__empleados)
        total = 0
        for A in self.__empleados:
            if(isinstance(A, Empleado)):
                total+=A.getSalario()
        return total/Temp
    
    def salarioMayor(self, x):
        for A in self.__empleados:
            if(isinstance(A, Empleado)):
                if(A.getSalario() > x):
                    print(A)
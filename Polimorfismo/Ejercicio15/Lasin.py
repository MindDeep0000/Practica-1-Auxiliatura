from multimethod import multimethod

class Ordenador:
    def __init__(self, cod_serie, num, ram, procesador, estado):
        self.__codigoSerial = cod_serie
        self.__numero = num
        self.__memoria = ram
        self.__procesador = procesador
        self.__estado = estado
    def getCodigoSerial(self):
        return self.__codigoSerial
    def getEstado(self):
        return self.__estado
    def getMemoria(self):
        return self.__memoria
    def __str__(self):
        return f"codigo serial({self.__codigoSerial}) numereo={self.__numero} memoria={self.__memoria}Gb, {self.__procesador}, <{self.__estado}>"

class Laboratorio:
    def __init__(self, nom, capacidad, n_ordenadores):
        self.__nombre = nom
        self.__capacidad = capacidad
        self.__n_ordenadores = n_ordenadores
        self.__ordenadores = []
    @multimethod
    def informacion(self, estado: str) -> None:
        """segun el estado"""
        for pc in self.__ordenadores:
            if(pc.getEstado() == estado):
                print(pc)
        
    @multimethod
    def informacion(self) -> None:
        """pertenecientes a un laboratorio dado"""
        for i in range(len(self.__ordenadores)):
            print(self.__ordenadores[i])
        
    @multimethod
    def informacion(self, tip: int) -> None:
        """mostrar ordenadores con mas de 8 de ram"""
        for pc in self.__ordenadores:
            if(pc.getMemoria() > tip):
                print(pc)
                
    def agregarOrdenador(self, nuevo):
        self.__ordenadores.append(nuevo)
    def getCods_seriales(self):
        lista = []
        for O in self.__ordenadores:
            lista.append(O.getCodigoSerial)
        return lista
    def trasladar(self, labo):
        labo.get_m_ordenadores.append(self.__ordenadores[0])
        labo.get_m_ordenadores.append(self.__ordenadores[1])
        self.__ordenadores.remove(0)
        self.__ordenadores.remove(1)
            
    def get_m_ordenadores(self):
        return self.__ordenadores
    
    def __str__(self):
        return f"nombre: {self.__nombre}\ncapacidad: {self.__capacidad}\nNro ordenadores: {self.__n_ordenadores}\n{self.get_m_ordenadores()}"

compu1 = Ordenador("serie1", 213, 4, "Intel Core", "activo")
compu2 = Ordenador("serie2", 13, 16, "AMD", "inactivo")
compu3 = Ordenador("serie3", 30, 16, "AMD", "activo")
compu4 = Ordenador("serie4", 100, 4, "Intel Core", "activo")
compu5 = Ordenador("serie5", 23, 8, "Intel Core", "inactivo")

lasin1 = Laboratorio("lasin1", 30, 12)
lasin2 = Laboratorio("lasin2", 15, 8)

lasin1.agregarOrdenador(compu1)
lasin1.agregarOrdenador(compu2)

lasin2.agregarOrdenador(compu3)
lasin2.agregarOrdenador(compu4)

lasin1.agregarOrdenador(compu5)

print("Todos los ordenadores del laboratorio")
lasin1.informacion()
print("Segun se estado")
lasin2.informacion("activo")
print("Segun sea mayor a la ram de 8GB")
lasin1.informacion(8)

print(lasin1)

lasin1.trasladar(lasin2)

print(lasin1)


from Bailarines import Bailarin
from Facultades import Facultad

class Fraternidad:
    def __init__(self, encargado, nombre):
        self.__encargado = encargado
        self.__nombre = nombre
        self.__integrantes = []
        self.__cantParticipantes = len(self.__integrantes)
        self.__facultades = []
        self.__fraternidades = []   
        
    def mismosParticipantes(self, fr):
        if(isinstance(fr, Fraternidad)):
            l1 = self.getIntegrantes()
            l2 = fr.getIntegrantes()
            listaCorta = min(l1, l2, key=len)
            listaLarga = max(l1, l2, key=len)
            
            for k in listaCorta:
                if(k in listaLarga):
                    print(f"<<< existe {k} en ambas fraternidades")
                    listaLarga.remove(k)
    
    def edadesIntegrantes(self):
        print("*** edades de los integrantes de la fraternidad")
        for I in self.__integrantes:
            if(isinstance(I, Bailarin)):
                print(f"bailarin: {I.getNombre()} edad: {I.getEdad()}")
    
    def agregarIntegrante(self, int, facultad, fraternidad):
        self.__integrantes.append(int)
        self.__facultades.append(facultad)
        self.__fraternidades.append(fraternidad)
        
    
    def verFraternidad(self):
        print("**** integrantes de la fraternidad")
        for i in range(len(self.__integrantes)):
            print(f"nombre: {self.__integrantes[i].getNombre()} facultad: {self.__facultades[i].getNombre()} fraternidad: {self.__fraternidades[i].getNombre()}")

    def verEncargados(self):
        print("*** encargados")
        print(f"fraternidad: {self.getNombre()} encargado: {self.getEncargado()}")

    def getIntegrantes(self):
        return self.__integrantes
    
    def getNombre(self):
        return self.__nombre
    
    def getEncargado(self):
        return self.__encargado
from libro import Libro
from multimethod import multimethod
class Estante:
    def __init__(self, tMaterial, tamanio, cMaxima_libros):
        self.__tMaterial = tMaterial
        self.__tamanio = tamanio
        self.__cMaxima = cMaxima_libros
        self.__libros = []
    
    def agregarLibros(self):
        pass
    
    def eliminarLibro(self, libro):
        pass
    
    def mostrarLibros(self):
        pass
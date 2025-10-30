from multimethod import multimethod
from Cancion import Cancion


class Playlist:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__canciones = []
        self.__nroCanciones = len(self.__canciones)
    @multimethod
    def agregarCancion(self, nCancion: Cancion) -> None:
        self.__canciones.append(nCancion)
    
    @multimethod
    def agregarCancion(self, canciones: list[Cancion]) -> None:
        for a in canciones:
            self.__canciones.append(a)
    
    def __str__(self):
        return f"nombre: {self.__nombre} nroCanciones: {self.__nroCanciones} canciones: {self.getCanciones()}"
    
    def getCanciones(self):
        info = "["
        for C in self.__canciones:
            info+=C.__str__()
            info+="\n"
        info+="]"
        return info
    
    def duracionTotal(self):
        duracion = 0
        for c in self.__canciones:
            duracion+=c.getDuracion()
        
        duracionMinutos = (duracion/60)
        return f"duracion en segundos {duracion}, duracion en minutos {duracionMinutos}"
    
    def buscarCancion(self, artista):
        for cancion in self.__canciones:
            if(cancion.getArtista() == artista):
                print(cancion)
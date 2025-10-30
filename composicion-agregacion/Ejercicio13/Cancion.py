class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.__titulo = titulo
        self.__artista = artista
        self.__duracionSegundos = duracion_segundos
    
    def getDuracion(self):
        return self.__duracionSegundos
    
    def getArtista(self):
        return self.__artista
    
    def __str__(self):
        return f"titulo: {self.__titulo} artista: {self.__artista} duracion: {self.__duracionSegundos} segundos"
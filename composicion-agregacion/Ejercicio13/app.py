from Cancion import Cancion
from playlist import Playlist

p1 = Playlist("playlist1")
#titulo, artista, duracion_segundos
p1.agregarCancion([Cancion("c1", "juan verde", 50), Cancion("tear up", "julian", 230), Cancion("this guy", "Maerlineas", 340), Cancion("fall", "Rodrigo", 843)])
print(p1.duracionTotal())
p1.buscarCancion("julian")

from multimethod import multimethod
from datetime import datetime


class Mp4:
    def __init__(self, marca, GBs, nro_canciones, canciones, nro_videos, videos):
        self.__marca = marca
        self.__capacidadGB = GBs
        self.__nroCanciones = nro_canciones
        self.__canciones = canciones
        self.__nroVideos = nro_videos
        self.__videos = videos
        self.fechaCreacion = datetime.now()

    @multimethod
    def eliminar(self, nombre: str) -> None:

        for j in range(len(self.__canciones[0]) - 1, -1, -1):
            if self.__canciones[0][j] == nombre:
                p_gigas = self.__canciones[2][j] / 1048576
                self.__capacidadGB += p_gigas
                del self.__canciones[0][j]
                del self.__canciones[1][j]
                del self.__canciones[2][j]
                self.__nroCanciones -= 1

                break

    @multimethod
    def eliminar(self, artista: str, tipo: int) -> None:
        for j in range(len(self.__canciones[0]) - 1, -1, -1):
            if self.__canciones[1][j] == artista:
                p_gigas = self.__canciones[2][j] / 1048576
                self.__capacidadGB += p_gigas
                del self.__canciones[0][j]
                del self.__canciones[1][j]
                del self.__canciones[2][j]
                self.__nroCanciones -= 1
                break

    @multimethod
    def eliminar(self, nombre: str, peso: float) -> None:
        for j in range(len(self.__canciones[0]) - 1, -1, -1):
            if self.__canciones[0][j] == nombre and self.__canciones[2][j] == peso:
                p_gigas = self.__canciones[2][j] / 1048576
                self.__capacidadGB += p_gigas
                del self.__canciones[0][j]
                del self.__canciones[1][j]
                del self.__canciones[2][j]
                self.__nroCanciones -= 1
                break

    def __add__(self, nueva_cancion):
        for i in range(len(self.__canciones[0])):
            if (
                nueva_cancion[0] == self.__canciones[0][i]
                and nueva_cancion[1] == self.__canciones[1][i]
            ):
                self.__canciones[0][i] = []
                self.__canciones[1][i] = []
                self.__canciones[2][i] = []
        self.__canciones[0].append(nueva_cancion[0])
        self.__canciones[1].append(nueva_cancion[1])
        self.__canciones[2].append(nueva_cancion[2])

        p_gigas = nueva_cancion[2] / 1048576
        self.__capacidadGB -= p_gigas
        self.__nroCanciones += 1

    def __sub__(self, nuevo_video):
        for i in range(len(self.__videos)):
            if (
                nuevo_video[0] == self.__videos[i][0]
                and nuevo_video[1] == self.__videos[i][1]
            ):
                self.__videos[i][0] = []
                self.__videos[i][1] = []
                self.__videos[i][2] = []
        self.__videos.append(nuevo_video)

        p_gigas = nuevo_video[2] / 1024
        self.__capacidadGB -= p_gigas
        self.__nroVideos += 1

    def __str__(self):
        return f"marca={self.__marca} capacidad={self.__capacidadGB}GB\nnro_canciones={self.__nroCanciones}\n{self.__canciones}\nnro_videos={self.__nroVideos}\n{self.__videos}\nfecha={self.fechaCreacion}"

    def capacidad(self):
        return round(self.__capacidadGB, 4)


reproductor = Mp4(
    "Toshiba",
    123.66,
    2,
    [["back To Black", "Lost On You"], ["Amy Winehouse", "LP"], [100, 150]],
    1,
    [["Heathens", "twenty one pilots", 50]],
)
print(reproductor.__str__())

reproductor + ["iron man", "Ozzy Osbourne", 20.4]

reproductor + ["lost for words", "David Gillmur", 10.7]

reproductor - ["Without Me", "Halsey", 30.3]

reproductor - ["Harmonica Andromeda", "KSHMR", 70.9]

print("")
print(reproductor.__str__())

reproductor.eliminar("back To Black")
reproductor.eliminar("LP", 0)
reproductor.eliminar("lost for words", 10.7)

print("")
print(reproductor.__str__())
print("capacidad total: ", reproductor.capacidad())

"""
    Ejercicio 2. Sea la clase Videojuego que tenga los atributos nombre, plataforma, cantidad
de jugadores. Se pide:
a) Instanciar al menos 2 videojuegos
b) Sobrecargar el constructor 2 veces
c) Sobrecargar el método agregarJugadores() para: agregar solo un jugador, y
agregar numero de jugadores según una cantidad ingresada por teclado.
"""

from multimethod import multimethod


class Videojuego:
    def __init__(self, *args):
        if len(args) == 3:
            self.nombre = args[0]
            self.plataforma = args[1]
            self.cantidadDeJugadores = args[2]
        elif len(args) == 2:
            if not isinstance(args[1], str):
                self.nombre = args[0]
                self.plataforma = None
                self.cantidadDeJugadores = args[1]
            else:
                self.nombre = args[0]
                self.plataforma = args[1]
                self.cantidadDeJugadores = 0

    @multimethod
    def agregarJugadores(self) -> None:
        self.cantidadDeJugadores += 1

    @multimethod
    def agregarJugadores(self, variosJugadores: int) -> None:
        self.cantidadDeJugadores = self.cantidadDeJugadores + variosJugadores

    def __str__(self):
        return f"Nombre: {self.nombre} plataforma: {self.plataforma} cantidad de jugadores: {self.cantidadDeJugadores}"


if __name__ == "__main__":
    borderlands = Videojuego("Borderlands", "steam")
    wow = Videojuego("World of warcraft", "Steam", 100000)

    print(borderlands.__str__())
    print(wow.__str__())
    borderlands.agregarJugadores(4)
    wow.agregarJugadores(200)
    print(borderlands.__str__())
    print(wow.__str__())

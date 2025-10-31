from Ropero import Ropero
from Ropa import Ropa

ropas = [Ropa("prenda de vestir femenina ligera y versátil", "algodón, lino o seda"),
        Ropa("uso formal o semiformal para hombres y mujeres", "lana, gabardina o paño"), 
        Ropa("ideal para ocasiones especiales como cócteles o ceremonias", "gasa, terciopelo, seda o encaje"),
        Ropa("Prenda de vestir infantil ideal", " poliéster")]

ropero = Ropero("Madera", ropas)
ropero.mostrarRopero()
ropero.eliminarPrendas("algodón")
ropero.eliminarPrendas("Prenda de vestir infantil", None)
ropero.mostrarPrendas("algodon", "ocaciones especiales")
ropero.agregarRopa(Ropa("M", "n"))
ropero.mostrarRopero()
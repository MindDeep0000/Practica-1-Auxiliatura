from Computadora import Computadora
from Ram import Ram
from DiscoDuro import DiscoDuro

ram1 = Ram(32, "marca 1", "ddr4")
ram2 = Ram(40, "marca 2", "ddr4")
ram3 = Ram(60, "marca 3", "ddr4")

d1 = DiscoDuro(1024, "marca1", "modelo1")
d2 = DiscoDuro(500, "marca1", "modelo1")
d3 = DiscoDuro(2048, "marca1", "modelo1")

pc1 = Computadora(año=2010, ram=ram1, discoDuro=d1)
pc2 = Computadora(año=2015, discoDuro=d2)
pc3 = Computadora(año=2020, ram=ram2)


print("computadora nueva 1")
print("*****************************************************************")
pc1.encender()

pc1.mostrar()

pc1.modificarCapacidad(23.7)
pc1.modificarCapacidad(112)

pc1.mostrar()
print("-----------------------------------------------------------------")

""" segunda commputadora"""
print("computadora nueva 2")
print("*****************************************************************")
pc2.encender()

pc2.mostrar()

pc2.modificarCapacidad(23.7)
pc2.modificarCapacidad(112)

pc2.mostrar()
print("-----------------------------------------------------------------")

"""" tercera computadora """
print("computadora nueva 3")
print("*****************************************************************")
pc3.encender()

pc3.mostrar()

pc3.modificarCapacidad(23.7)
pc3.modificarCapacidad(112)

pc3.mostrar()
print("-----------------------------------------------------------------")

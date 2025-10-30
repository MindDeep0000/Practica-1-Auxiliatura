from Orden import orden
from Ventas import ventas
from Plato import plato


o1 = orden(fecha="10-10-25", hora="10am", nroPedido=1, np=11, nomCli="Joel", apeCli="Barrera Quispe", ciCli=12321421)
o1.agregarPlatos([plato("plato1", 21), plato("plato2", 32), plato("plato3", 123)])

o2 = orden(fecha="5-7-25", hora="8am", nroPedido=2, np=22, nomCli="Alberto", apeCli="Cerati", ciCli=48320311)
o2.agregarPlatos([plato("plato21", 31), plato("plato22", 61), plato("plato23", 31)])

o3 = orden(fecha="9-12-25", hora="9pm", nroPedido=3, np=33, nomCli="Norberta", apeCli="Achu", ciCli=84737292)
o3.agregarPlatos([plato("plato31", 482), plato("plato32", 37), plato("plato33", 12)])

o4 = orden(fecha="1-1-25", hora="7pm", nroPedido=4, np=44, nomCli="Gabriela", apeCli="Zapata", ciCli=84829212)
o4.agregarPlatos([plato("plato41", 41), plato("plato42", 37), plato("plato43", 11)])

o5 = orden(fecha="1-7-25", hora="9am", nroPedido=5, np=55, nomCli="Carlos", apeCli="pinto", ciCli=94203214)
o5.agregarPlatos([plato("plato51", 53), plato("plato52", 482), plato("plato53", 94)])

v1 = ventas("san miguel")
v1.agregarOrden(o1)
v1.agregarOrden(o2)
v1.agregarOrden(o3)
v1.agregarOrden(o4)
v1.agregarOrden(o5)
print("Buscar orden deacuerdo a una fecha")
v1.getPedidosEnFechaX("1-1-25")

print("Mostrar ordenes segun el total de los precios de los platos")
v1.ordenarOrdenes()
v1.mostrarOrdenes()

print("Eliminar orden deacuerdo al ci del cliente")
v1.eliminarOrden(12321421)
v1.mostrarOrdenes()
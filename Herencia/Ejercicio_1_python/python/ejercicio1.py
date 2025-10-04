class Persona:

    def __init__(self, nombre, apellido, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci

    def method(self):
        pass
class Jefe(Persona):
    def __init__(self, sucursal, CI, tipo, nombre, apellido):
        super().__init__(nombre, apellido, CI)
        self.sucursal = sucursal
        self.CI = CI
        self.tipo = tipo

    def method(self):
        print("Guiar a su personal")
class Cliente(Persona):
    def __init__(self, nro_compra, id_cliente, nombre, apellido, ci):
        super().__init__(nombre, apellido, ci)
        self.nro_compra = nro_compra
        self.id_cliente = id_cliente
        self.nombre = nombre

    def method(self):
        print("Comprar")

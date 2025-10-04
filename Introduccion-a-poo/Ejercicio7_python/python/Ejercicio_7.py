class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia

    def alimentar(self, mas_energia, maximo):
        aux = self.energia + mas_energia
        if aux > maximo:
            print("tu mascota esta con demasiada energia")
        else:
            self.energia += mas_energia

    def jugar(self, menos_energia, minimo):
        resta = self.energia - menos_energia
        if resta < minimo:
            print("Tu mascota ya esta mu canasada, dejala descanzar")
        else:
            self.energia -= menos_energia

    def estado_actual(self):
        return f"nombre: {self.nombre}, tipo: {self.tipo}, energia: {self.energia} (percent)"

canino1 = Mascota("Petardo", "pulgoso", 100)
canino2 = Mascota("Chamillo", "cachuchin", 80)

print(canino1.estado_actual())
print("alimentar +32 maximo: 100")
canino1.alimentar(32, 100)
print("jugar -50 minimo 30")
canino1.jugar(50, 30)
print(canino1.estado_actual())
print("")

print(canino2.estado_actual())
print("alimentar +60 maximo 90")
canino2.alimentar(60, 90)
print("jugar -70 minimo 10")
canino2.jugar(70, 10)
print(canino2.estado_actual())
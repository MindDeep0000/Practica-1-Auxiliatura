import json
from charango import Charango

class GestorCharangos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.charangos = []

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.charangos = [Charango.from_dict(d) for d in data]
        except FileNotFoundError:
            self.charangos = []

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump([c.to_dict() for c in self.charangos], f, indent=4)

    # b) Eliminar charangos con más de 6 cuerdas en false
    def eliminar_con_muchas_cuerdas_false(self):
        self.charangos = [
            c for c in self.charangos
            if c.cuerdas.count(False) <= 6
        ]

    # c) Listar charangos por material
    def listar_por_material(self, material):
        return [c for c in self.charangos if c.material == material]

    # d) Buscar los charangos con 10 cuerdas
    def buscar_con_diez_cuerdas(self):
        return [c for c in self.charangos if c.nro_cuerdas == 10]

    # e) Ordenar por material alfabéticamente
    def ordenar_por_material(self):
        self.charangos.sort(key=lambda c: c.material)

class Charango:
    def __init__(self, material, nro_cuerdas, cuerdas):
        self.material = material
        self.nro_cuerdas = nro_cuerdas
        self.cuerdas = cuerdas  # lista de booleanos

    def to_dict(self):
        return {
            "material": self.material,
            "nro_cuerdas": self.nro_cuerdas,
            "cuerdas": self.cuerdas
        }

    @staticmethod
    def from_dict(data):
        return Charango(data["material"], data["nro_cuerdas"], data["cuerdas"])

class Alimento:
    def __init__(self, nombre, fecha_vencimiento, cantidad):
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fecha_vencimiento": self.fecha_vencimiento,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(d):
        return Alimento(d["nombre"], d["fecha_vencimiento"], d["cantidad"])

    def __str__(self):
        return f"{self.nombre} | vence: {self.fecha_vencimiento} | cant: {self.cantidad}"

from dataclasses import dataclass


@dataclass
class Estudiante:
    ru: int
    nombre: str
    paterno: str
    materno: str
    edad: int

    def to_dict(self) -> dict:
        return {
            "ru": self.ru,
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "edad": self.edad,
        }

    @staticmethod
    def from_dict(d: dict) -> 'Estudiante':
        return Estudiante(d["ru"], d["nombre"], d.get("paterno", ""), d.get("materno", ""), d.get("edad", 0))

    def __str__(self) -> str:
        return f"{self.nombre} {self.paterno} {self.materno} (RU={self.ru}) age={self.edad}"

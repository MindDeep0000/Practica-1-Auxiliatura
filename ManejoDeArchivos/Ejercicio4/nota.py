from dataclasses import dataclass
from typing import Dict
from estudiante import Estudiante


@dataclass
class Nota:
    materia: str
    nota_final: float
    estudiante: Estudiante

    def to_dict(self) -> Dict:
        return {
            "materia": self.materia,
            "nota_final": self.nota_final,
            "estudiante": self.estudiante.to_dict(),
        }

    @staticmethod
    def from_dict(d: Dict) -> 'Nota':
        est = Estudiante.from_dict(d["estudiante"])
        return Nota(d.get("materia", ""), float(d.get("nota_final", 0.0)), est)

    def __str__(self) -> str:
        return f"{self.estudiante.nombre} ({self.estudiante.ru}) - {self.materia}: {self.nota_final}"

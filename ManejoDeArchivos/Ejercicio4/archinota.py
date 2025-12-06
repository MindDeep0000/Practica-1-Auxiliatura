import json
import os
from typing import List, Optional
from nota import Nota
from estudiante import Estudiante


class ArchiNota:

    def __init__(self, filename: str = "notas.json"):
        # ensure the JSON file is placed inside the Ejercicio4 package directory
        if os.path.isabs(filename):
            self.filename = filename
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            # ensure directory exists
            if not os.path.isdir(base_dir):
                os.makedirs(base_dir, exist_ok=True)
            self.filename = os.path.join(base_dir, filename)

    def crear_archivo(self) -> None:
        # ensure directory exists for the filename and create an empty JSON array if missing
        dirn = os.path.dirname(self.filename)
        if dirn and not os.path.isdir(dirn):
            os.makedirs(dirn, exist_ok=True)
        try:
            with open(self.filename, "x", encoding="utf-8") as f:
                f.write("[]")
        except FileExistsError:
            # if file exists but is empty, ensure it contains a JSON array
            try:
                if os.path.getsize(self.filename) == 0:
                    with open(self.filename, "w", encoding="utf-8") as f:
                        f.write("[]")
            except OSError:
                pass

    def leer_notas(self) -> List[Nota]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
        notas: List[Nota] = []
        for item in data:
            try:
                notas.append(Nota.from_dict(item))
            except Exception:
                continue
        return notas

    def guardar_notas(self, notas: List[Nota]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([n.to_dict() for n in notas], f, ensure_ascii=False, indent=2)

    def agregar_notas(self, notas: List[Nota]) -> None:
        todas = self.leer_notas()
        todas.extend(notas)
        self.guardar_notas(todas)

    def agregar_estudiantes(self, estudiantes: List[Estudiante], materia: str, nota_default: float = 0.0) -> None:
        notas = [Nota(materia=materia, nota_final=nota_default, estudiante=est) for est in estudiantes]
        self.agregar_notas(notas)

    def promedio_total(self) -> Optional[float]:
        notas = self.leer_notas()
        if not notas:
            return None
        total = sum(n.nota_final for n in notas)
        return total / len(notas)

    def mejores(self) -> List[Nota]:
        notas = self.leer_notas()
        if not notas:
            return []
        max_n = max(n.nota_final for n in notas)
        return [n for n in notas if n.nota_final == max_n]

    def ordenar_por_materia(self, materia: str, descending: bool = True) -> List[Nota]:
        notas = [n for n in self.leer_notas() if n.materia == materia]
        notas.sort(key=lambda x: x.nota_final, reverse=descending)
        return notas

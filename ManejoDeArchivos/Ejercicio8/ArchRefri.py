import json
import os
class ArchRefri:
    def __init__(self, nombre, archivo_json="Ejercicio8/datos.json"):
        self.nombre = nombre
        self.archivo_json = archivo_json
        self.alimentos = []

        # Crea carpeta si no existe
        os.makedirs("Ejercicio8", exist_ok=True)

        # Si el archivo existe, cargarlo
        if os.path.exists(self.archivo_json):
            self.cargar_json()
        else:
            self.guardar_json()  # crea archivo vacío inicial

    # -------------------- CRUD --------------------

    def crear(self, alimento):
        self.alimentos.append(alimento)
        self.guardar_json()

    def modificar_por_nombre(self, nombre, nueva_fecha, nueva_cantidad):
        for a in self.alimentos:
            if a.nombre.lower() == nombre.lower():
                a.fecha_vencimiento = nueva_fecha
                a.cantidad = nueva_cantidad
                self.guardar_json()
                return True
        return False

    def eliminar_por_nombre(self, nombre):
        for a in self.alimentos:
            if a.nombre.lower() == nombre.lower():
                self.alimentos.remove(a)
                self.guardar_json()
                return True
        return False

    # -------------------- CONSULTAS --------------------

    def mostrar_caducados_antes_de(self, fecha_x):
        for a in self.alimentos:
            if a.fecha_vencimiento < fecha_x:
                print(a)

    def eliminar_cantidad_cero(self):
        self.alimentos = [a for a in self.alimentos if a.cantidad != 0]
        self.guardar_json()

    def mostrar_vencidos(self, fecha_hoy):
        for a in self.alimentos:
            if a.fecha_vencimiento < fecha_hoy:
                print(a)

    def mostrar_mayor_cantidad(self):
        if not self.alimentos:
            print("No hay alimentos.")
            return

        mayor = max(self.alimentos, key=lambda a: a.cantidad)
        print("Mayor cantidad:", mayor)

    def mostrar_todos(self):
        for a in self.alimentos:
            print(a)

    # -------------------- JSON --------------------

    def guardar_json(self):
        lista = [a.to_dict() for a in self.alimentos]
        with open(self.archivo_json, "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

    def cargar_json(self):
        with open(self.archivo_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
            self.alimentos = [Alimento.from_dict(d) for d in datos]

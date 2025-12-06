import json
import os

# Crear la carpeta Ejercicio7 si no existe
if not os.path.exists("Ejercicio7"):
    os.makedirs("Ejercicio7")

# Clase Persona
class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.ci = ci

    def __str__(self):
        return f"{self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} (CI: {self.ci})"

# Clase Niño que hereda de Persona
class Niño(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, ci, edad, peso, talla):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, ci)
        self.edad = edad
        self.peso = peso
        self.talla = talla

    def __str__(self):
        return f"{super().__str__()} - Edad: {self.edad}, Peso: {self.peso}, Talla: {self.talla}"

# Clase Archivo de Niños
class ArchNiño:
    def __init__(self, na):
        self.na = na
        self.ninos = self._leer_archivo()

    def _leer_archivo(self):
        try:
            with open(f"Ejercicio7/{self.na}", "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Niño(**n) for n in data]
        except FileNotFoundError:
            return []

    def crearArchivo(self):
        with open(f"Ejercicio7/{self.na}", "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    def guardaNiño(self, n: Niño):
        self.ninos.append(n)
        self._guardar_en_archivo()

    def _guardar_en_archivo(self):
        with open(f"Ejercicio7/{self.na}", "w", encoding="utf-8") as f:
            json.dump([n.__dict__ for n in self.ninos], f, indent=4)

    def listarNiños(self):
        for n in self.ninos:
            print(n)

    def promedioEdad(self):
        if not self.ninos:
            return 0
        return sum(n.edad for n in self.ninos) / len(self.ninos)

    def buscarNiñoPorCI(self, ci):
        for n in self.ninos:
            if n.ci == ci:
                return n
        return None

    def niñoMayorTalla(self):
        if not self.ninos:
            return None
        return max(self.ninos, key=lambda n: n.talla)

    def pesoAdecuado(self):
        # Definimos peso adecuado según talla y edad (ejemplo simple: BMI aproximado)
        adecuados = []
        for n in self.ninos:
            bmi = n.peso / (n.talla ** 2)  # peso / talla^2
            if 14 <= bmi <= 18:  # rango de ejemplo
                adecuados.append(n)
        return adecuados

    def mostrarNoAdecuado(self):
        # Mostrar niños que no tienen peso adecuado
        return [n for n in self.ninos if n not in self.pesoAdecuado()]

# --- EJEMPLO DE USO ---
archivo = ArchNiño("ninos.json")

# Crear archivo vacío si no existe
if not archivo.ninos:
    archivo.crearArchivo()

# Agregar niños
archivo.guardaNiño(Niño("Juan", "Perez", "Lopez", "123456", 10, 32, 1.4))
archivo.guardaNiño(Niño("Maria", "Gomez", "Diaz", "654321", 8, 25, 1.3))
archivo.guardaNiño(Niño("Pedro", "Sanchez", "Martinez", "789012", 12, 50, 1.5))

# Listar todos los niños
print("Listado de niños:")
archivo.listarNiños()

# Promedio de edad
print("Promedio de edad:", archivo.promedioEdad())

# Buscar niño por CI
ci_buscar = "123456"
n = archivo.buscarNiñoPorCI(ci_buscar)
print(f"Niño con CI {ci_buscar}:", n)

# Niño con la talla más alta
print("Niño con la talla más alta:", archivo.niñoMayorTalla())

# Niños con peso adecuado
print("Niños con peso adecuado:")
for n in archivo.pesoAdecuado():
    print(n)

# Niños que no tienen peso adecuado
print("Niños sin peso adecuado:")
for n in archivo.mostrarNoAdecuado():
    print(n)

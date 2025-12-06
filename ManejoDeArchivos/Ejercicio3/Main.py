import json
import os

# Crear la carpeta Ejercicio3 si no existe
if not os.path.exists("Ejercicio3"):
    os.makedirs("Ejercicio3")

# Clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto(codigo={self.codigo}, nombre='{self.nombre}', precio={self.precio})"

# Clase ArchivoProducto
class ArchivoProducto:
    def __init__(self, nomA):
        self.nomA = nomA
        # Intentamos leer el archivo si ya existe
        self.productos = self._leer_archivo()

    def _leer_archivo(self):
        try:
            with open(f"Ejercicio3/{self.nomA}", "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Producto(**p) for p in data]
        except FileNotFoundError:
            return []

    def crearArchivo(self):
        with open(f"Ejercicio3/{self.nomA}", "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    def guardaProducto(self, p: Producto):
        self.productos.append(p)
        self._guardar_en_archivo()

    def _guardar_en_archivo(self):
        with open(f"Ejercicio3/{self.nomA}", "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in self.productos], f, indent=4)

    def buscaProducto(self, c: int):
        for p in self.productos:
            if p.codigo == c:
                return p
        return None

    def promedioPrecios(self):
        if not self.productos:
            return 0
        return sum(p.precio for p in self.productos) / len(self.productos)

    def productoMasCaro(self):
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.precio)

# --- EJEMPLO DE USO ---
archivo = ArchivoProducto("productos.json")

# Crear archivo vacío si no existe
if not archivo.productos:
    archivo.crearArchivo()

# Agregar productos
archivo.guardaProducto(Producto(1, "Producto A", 100.0))
archivo.guardaProducto(Producto(2, "Producto B", 250.0))
archivo.guardaProducto(Producto(3, "Producto C", 180.0))

# Buscar un producto
p = archivo.buscaProducto(2)
print("Producto buscado:", p)

# Calcular promedio de precios
print("Promedio de precios:", archivo.promedioPrecios())

# Producto más caro
print("Producto más caro:", archivo.productoMasCaro())

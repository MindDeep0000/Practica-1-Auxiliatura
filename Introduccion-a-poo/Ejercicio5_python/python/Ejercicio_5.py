class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci

    def mostrar_datos(self):
        return f"nombre completo: {self.nombre} {self.paterno} {self.materno} edad: {self.edad} c.i.: {self.ci}"

    def mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad"
        return f"{self.nombre} no es mayor de edad"

    def modificar_edad(self, nuevo):
        self.edad = nuevo

    def tocayo(self, nueva):
        if self.paterno == nueva.paterno:
            return "Comparten el mismo apellido"
        return "No comparten similitud en los apellidos"

p1 = Persona("Jordi", "Andrade", "Gotret", 35, 12781234)
p2 = Persona("Mary", "Andrade", "Arabi", 18, 34129090)

print(p1.mostrar_datos())
print(p2.mostrar_datos())

print(p1.mayor_de_edad())
print(p2.mayor_de_edad())

print("Modificando la edad de Jordi")
p1.modificar_edad(32)
print(p1.mostrar_datos())

print(p1.tocayo(p2))
class Procesador:
    def __init__(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    def __str__(self):
        return f"{self.modelo} {self.velocidad}GHz"


class MemoriaRam:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad}GB {self.tipo}"


class DiscoDuro:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return f"{self.capacidad}GB {self.tipo}"


class Computador:
    def __init__(self, ma, mProc, vProc, cRam, tRam, cDD, tDD):
        self.marca = ma
        self.procesador = Procesador(mProc, vProc)
        self.memoria = MemoriaRam(cRam, tRam)
        self.disco = DiscoDuro(cDD, tDD)
        self.programas = []

    def instalar_programa(self, prog):
        self.programas.append(prog)

    def mostrar_programas_instalados(self):
        for prog in self.programas:
            print("- " + prog)

    def mostrar_especificaciones(self):
        print("Procesador: " + str(self.procesador))
        print("Memoria ram: " + str(self.memoria))
        print("Disco duro: " + str(self.disco))
        print("Programas instalados")
        self.mostrar_programas_instalados()

    def __del__(self):
        print("Eliminar computador")


if __name__ == "__main__":
    lenovo = Computador("Lenovo", "i7", 5.7, 120, "sd", 2, "solido")
    lenovo.instalar_programa("Adobe photoshop")
    lenovo.instalar_programa("markdown")
    lenovo.instalar_programa("memreduct")
    lenovo.instalar_programa("mozilla")
    lenovo.mostrar_especificaciones()
    # In Python, memory management is automatic, so no need to manually free memory or call garbage collector.
    lenovo = None
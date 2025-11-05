from Charla import Charla


class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.C = []
        self.nc = len(self.C)

    def agregarCharla(self, ch):
        mayor = 0
        self.C.append(ch)
        if isinstance(ch, Charla):
            if ch.np != 0 or ch.np != 1:
                for i in range(len(self.C) - 1):
                    mayor = self.C[i].np
                    for j in range(i + 1, len(self.C)):
                        if self.C[j].np >= mayor:
                            elemento = self.C.pop(i)
                            self.C.insert(j, elemento)
            else:
                self.C.append(ch)

    def existePersona(self, nombre, ci):
        alerte = False
        for K in self.C:
            datos = K.datosSpeaker()
            if datos["nombre"] == nombre and datos["ci"] == ci:
                print(f"El speaker esta dando la charla de {K.nombreCharla}")
                alerte = True
                break

            if K.buscarParticipante(nombre, ci):
                print(f"Dado por el speaker {K.S.nombre} de edad {K.S.edad}")
                alerte = True
                break
        if(not alerte):
            print("No se encontro el registro especificado de la persona")

    def eliminarSpeaker(self, ci):
        for J in self.C:
            if isinstance(J, Charla):
                if J.S.ci == ci:
                    J.S = None
                    self.C.remove(J)
                    print("speaker eliminando exitosamente")
                    break

    def calcularProEdades(self):
        totalPart = 0
        totalEdades = 0
        for A in self.C:
            if isinstance(A, Charla):
                totalPart += A.np
                totalEdades += A.calcularTotal()
        return totalEdades // totalPart

    def mostrarCharlas(self):
        for K in self.C:
            print(K.mostrar())

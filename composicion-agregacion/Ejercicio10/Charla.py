from herencia import Participante
from herencia import Speaker

class Charla:
    def __init__(self, lugar, nmCharla, nombre, apellido, edad, ci, esp):
        self.lugar = lugar
        self.nombreCharla = nmCharla
        self.S = Speaker(nombre, apellido, edad, ci, esp)
        self.participantes = []
        self.np = len(self.participantes)
    
    def agregarParticipante(self, p):
        self.participantes.append(p)
        self.np = len(self.participantes)
    
    def calcularTotal(self):
        total = 0
        if(len(self.participantes)!=0):
            for a in self.participantes:
                if(isinstance(a, Participante)):
                    total+=a.getEdad()
            return total
        else:
            print("lista vacia")
            return -1
    
    def datosSpeaker(self):
        # nombre: str, ci: int
        return { "nombre":{self.S.nombre}, "ci":{self.S.ci} } 
    
    def buscarParticipante(self, nombre, ci):
        for A in self.participantes:
            if(isinstance(A, Participante)):
                if(A.nombre==nombre and A.ci==ci):
                    print(f"participante {A.nombre} esta en la charla {self.nombreCharla}")
                    return True
        return False
    
    def mostrar(self):
        return f"N: {self.nombreCharla} np:{self.np} Speaker: {self.S.nombre}"
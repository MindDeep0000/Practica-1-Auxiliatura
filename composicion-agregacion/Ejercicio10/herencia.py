class Persona: 
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci
    
    def getEdad(self):
        return self.edad

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        self.especialidad = especialidad
        super().__init__(nombre, apellido, edad, ci)
    

class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket


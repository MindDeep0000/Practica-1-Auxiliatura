from Estudiante import estudiante

class carrera:
    def __init__(self, nombre=None):
        self.__nombre = nombre
        self.lista = []
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def agregarEstudiante(self, nEst):
        self.lista.append(nEst)
    
    def eliminarEstudiante(self, est):
        self.lista.remove(est)
        
    def obtenerLista(self):
        return self.lista
        
    def contar_estudiantes(self):
        return len(self.lista)

    def buscar_estudiante(self, matricula):
        for e in self.lista:
            if isinstance(e, estudiante):
                if(e.getMatricula() == matricula):
                    print(e)
                    return True
        return False
    
    def cambiar_carrera(self, n_carrera, est):
        if isinstance(est, estudiante):
            self.eliminarEstudiante(est)
            n_carrera.agregarEstudiante(est)
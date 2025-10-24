from Carrera import carrera

class facultad:
    def __init__(self, nombre=None, nroCarreras=None):
        self.__nombre = nombre
        self.__nroCarreras = nroCarreras
        self.carrera1 = carrera()
        self.carrera2 = carrera()
        self.carrera3 = carrera()
        self.lista_carreras=[]
    
    def set_facultad(self, nombre, nroCarreras):
        self.__nombre = nombre
        self.__nroCarreras = nroCarreras
        
    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"{self.__nombre}"
    
    def modificar_carrera1(self, nomCarrera):
        self.carrera1.setNombre(nomCarrera)
        self.lista_carreras.append(self.carrera1)
    
    def modificar_carrera2(self, nomCarrera):
        self.carrera2.setNombre(nomCarrera)
        self.lista_carreras.append(self.carrera2)
        
    def modificar_carrera3(self, nomCarrera):
        self.carrera3.setNombre(nomCarrera)
        self.lista_carreras.append(self.carrera3)
    
    def agregarEst_carrera1(self, est):
        self.carrera1.agregarEstudiante(est)
    
    def agregarEst_carrera2(self, est):
        self.carrera2.agregarEstudiante(est)
        
    def agregarEst_carrera3(self, est):
        self.carrera3.agregarEstudiante(est)
    
    def getNombreCarrera1(self):
        return self.carrera1.getNombre()
    
    def getNombreCarrera2(self):
        return self.carrera2.getNombre()
    
    def getNombreCarrera3(self):
        return self.carrera3.getNombre()
    
    def nroEstCarrera1(self):
        return self.carrera1.contar_estudiantes()
    
    def nroEstCarrera2(self):
        return self.carrera2.contar_estudiantes()
        
    def nroEstCarrera3(self):
        return self.carrera3.contar_estudiantes()

    def buscarEstudiante_facultad1(self, matricula):
        if(self.carrera1.buscar_estudiante(matricula)):
            return True
        
        elif(self.carrera2.buscar_estudiante(matricula)):
            return True
        
        elif(self.carrera3.buscar_estudiante(matricula)):
            return True
        
        else:
            return False
    
    def cambio_carrera(self, antigua, nueva, estudiante, facultad):
        if(self.getNombre() == facultad):
            carrera_antigua = self.buscarCarrera(antigua)
            carrera_nueva = self.buscarCarrera(nueva)
            if(carrera_nueva!=None and carrera_antigua!=None):
                carrera_antigua.cambiar_carrera(carrera_nueva, estudiante)
                return True
            else:
                print("error al encontrar la carrera")
                return False
        else:
            print("error al encontrar la facultad")
    
    # def cantidad_estudiantes(self):
    #     return self.carrera.cantidad_estudiantes()

    def buscarCarrera(self, nombre):
        if(nombre==self.carrera1.getNombre()):
            return self.carrera1
        elif(nombre==self.carrera2.getNombre()):
            return self.carrera2
        elif(nombre==self.carrera3.getNombre()):
            return self.carrera3
        else:
            return None
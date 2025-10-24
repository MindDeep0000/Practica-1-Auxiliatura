from Facultad import facultad

class universidad:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.fac1 = facultad()
        self.fac2 = facultad()
        self.lista_rectores=[]
        self.lista_facultades=[]
    
    def agregar_rector(self, rector):
        self.lista_rectores.append(rector)
    
    def modificar_facultad1(self, nomFacultad, nroCarreras):
        self.fac1.set_facultad(nomFacultad, nroCarreras)
        self.lista_facultades.append(self.fac1)
    
    def modificar_facultad2(self, nomFacultad, nroCarreras):
        self.fac2.set_facultad(nomFacultad, nroCarreras)
        self.lista_facultades.append(self.fac2)
    
    def agregar_carrera1_facultad1(self, nombre):
        self.fac1.modificar_carrera1(nombre)
    
    def agregar_carrera2_facultad1(self, nombre):
        self.fac1.modificar_carrera2(nombre)
    
    def agregar_carrera3_facultad1(self, nombre):
        self.fac1.modificar_carrera3(nombre)
    
    def agregarEstudiante_carrera1_facultad1(self, est):
        self.fac1.agregarEst_carrera1(est)
        
    def agregarEstudiante_carrera2_facultad1(self, est):
        self.fac1.agregarEst_carrera2(est)
        
    def agregarEstudiante_carrera3_facultad1(self, est):
        self.fac1.agregarEst_carrera3(est)
    
    def contarEstudiantes(self):
        print(f"carrera1: {self.fac1.getNombreCarrera1()} {self.fac1.nroEstCarrera1()}")
        print(f"carrera2: {self.fac1.getNombreCarrera2()} {self.fac1.nroEstCarrera2()}")
        print(f"carrera3: {self.fac1.getNombreCarrera3()} {self.fac1.nroEstCarrera3()}")
    
    def buscar_estudiante(self, matricula):
        if(self.fac1.buscarEstudiante_facultad1(matricula)):
            return f"Estudiante de la facultad de : {self.fac1}"
        else:
            return f"Estudiante no encontrado"
    
    def cambiarCarrera(self, antigua, nueva, estudiante, facultad):
        if(self.fac1.cambio_carrera(antigua, nueva, estudiante, facultad)):
            print("Cambio de carrera realizado con exito")
        else:
            print("Ha ocurrido un error")
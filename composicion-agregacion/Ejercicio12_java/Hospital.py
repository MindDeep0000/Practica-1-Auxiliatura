class Hospital:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__doctores = []
        self.__cantDoctores = len(self.__doctores)
    
    def agregarDoctor(self, dr):
        self.__doctores.append(dr)
    
    def mostrarDoctores(self):
        print(f"*** {self.__nombre}\n<<doctores>>")
        for d in self.__doctores:
            print(d)
class discoDuro:
    def __init__(self, tipo, cantMemoria):
        self.__tipo = tipo
        self.__memoria = cantMemoria
    
    def __str__(self):
        return f"tipo: {self.__tipo} memoria: {self.__memoria}"
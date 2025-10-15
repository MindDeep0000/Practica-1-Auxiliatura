class laptop:
    def __init__(self, micro=None, ram=None, DiscoDuro=None, Bateria=None):
        self.__microprocesador = micro
        self.__cantRam = ram
        self.__DiscoDuro = DiscoDuro
        self.bateria = Bateria

    def __str__(self):
        return f"micro: {self.__microprocesador} RAM: {self.__cantRam} hard disk: {self.__DiscoDuro}\n{self.bateria}"
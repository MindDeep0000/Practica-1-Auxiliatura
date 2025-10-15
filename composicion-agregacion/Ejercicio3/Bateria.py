class bateria:
    def __init__(self, amp, material):
        self.__amperaje = amp
        self.__material = material
    
    def __str__(self):
        return f"amperaje: {self.__amperaje} material: {self.__material}"
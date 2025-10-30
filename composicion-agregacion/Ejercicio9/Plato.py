class plato:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    def __str__(self):
        return f"nombre: {self.__nombre} precio: {self.__precio}"
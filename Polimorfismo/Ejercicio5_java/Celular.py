"""
    Ejercicio 5. Dada la clase celular <nroTel, dueño, espacio, ram, nroApp>
a) realizar el diagrama de clases
b) realizar la sobrecarga del operador ++ para aumentar en 10 el nroApp.
c) realizar la sobrecarga del operador - - para disminuir el espacio en 5 gb.
d) mostrar los datos antes y después de los operadores.
"""

class Celular:
    def __init__(self, nroDeTelefono, nombre, espacio, ram, nroApp):
        self.__nroTelefono = nroDeTelefono
        self.__dueño = nombre
        self.__espacio = espacio
        self.__ram = ram
        self.__nroApp = nroApp
    
    def iadd(self):
        self.__nroApp += 10
    
    def dsub(self):
        self.__espacio -= 5
        self.__espacio = round(self.__espacio, 2)
    
    def __str__(self):
        return f"nro: {self.__nroTelefono} - dueño: {self.__dueño} - espacio: {self.__espacio} GB - ram: {self.__ram} GB - nroApps: {self.__nroApp}"
    

celular = Celular(78929330, "Joel", 6.44, 10, 20)
print(celular.__str__())
celular.iadd()
celular.dsub()
print(celular.__str__())
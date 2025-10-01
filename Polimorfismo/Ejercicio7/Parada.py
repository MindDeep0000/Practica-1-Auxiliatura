from multimethod import multimethod
class Parada:
    def __init__(self, admins=None, autos=None, nombreP=None):
        
        if(admins!=None and autos!=None and nombreP!=None):
            self.__admins = admins
            self.__autos = autos
            self.__nombreP = nombreP
        else:
            self.__admins = [
                "Jose A.",
                "Ben H.",
                "Carla M.",
                "Joel B.",
                "Gustavo S.",
                "Fabio L.",
                "Carol B.",
                "Gerardo J.",
                "Lucio V.",
                
            ]
            self.__autos = [
                ["Toyota", "Rojo Morales", "2341KFEG"],
                ["Nissan", "Flabio Josefo", "5785KLGE"],
                ["Subaru", "Jose Miguel Suarez", "6294LLIA"],
                ["Suzuki", "Matilda Guerrero", "3671JJSKK"],
                ["Mitsubishi", "Pablo Hurarte", "3282SHTKA"],
                ["Mazda", "Lucia Quiroga", "4287GWQN"],
                ["Tesla", "Paola Abdul", "4843JSNE"],
                ["Honda", "Dina Pique", "4724REGN"],
                ["Ford", "John Palmer", "2613HRBS"],
                
            ]
            self.__nombreP = "Los Andes"     
    def mostrar(self):
        for i in range(len(self.__admins)):
            print(self.__admins[i], end=" ")
        print("")
        
        for j in range(len(self.__autos)):
            print(self.__autos[j])
        
        print(self.__nombreP)
    @multimethod
    def adicionar(self, nuevoAdmin: str) -> None:
        if(len(self.__admins)<10):
            self.__admins.append(nuevoAdmin)
            print("Agregado exitosamente.")
        else:
            print("No es posible añadir mas registros")
    @multimethod
    def adicionar(self, nuevoAdmin: str, indice: int) -> None:
        if(indice>=0 and indice<=10):
            self.__admins[indice] = nuevoAdmin
            print("Agregado exitosamente.")
        else:
            print("No es posible añadir mas registros")
    @multimethod
    def adicionar(self, modelo: str, conductor: str, placa: str) -> None:
        if(len(self.__autos)<10):
            self.__autos.append([modelo, conductor, placa])
            print("Agregado exitosamente.")
        else:
            print("No es posible añadir el registro")
    @multimethod
    def adicionar(self, modelo: str, conductor: str, placa: str, indice: int) -> None:
        if(indice<=10 and indice>=0):
            self.__autos[indice] = [modelo, conductor, placa]
            print("Agregado exitosamente.")
        else:
            print("No es posible añadir el registro")

p1 = Parada()
p1.adicionar("Mel Brucks (nuevo)")
p1.adicionar("Toyosa", "Joel Blanco (nuevo)", "3429JFHS")
p1.mostrar()
p1.adicionar("Jonh Malkovich (nuevo)", 3)
p1.adicionar("Toyosa", "Ruth Valencia (nuevo)", "4832HFJE", 4)
p1.mostrar()
p1.adicionar("none")
p1.adicionar("tres", "kkk", "eeee")
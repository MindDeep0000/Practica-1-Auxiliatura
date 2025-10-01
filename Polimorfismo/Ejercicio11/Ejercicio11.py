class Crucero:
    def __init__(self, nomb, pOrigen, pDestino, nroPasajeros, m_pasajeros):
        self.__nombre = nomb
        self.__paisOrigen = pOrigen
        self.__paisDestino = pDestino
        self.__nroPasajeros = nroPasajeros
        self.__pasajeros = m_pasajeros
        
    def __set__(self, nuevo):
        self.__pasajeros.append(nuevo.__get__())
        self.__nroPasajeros+=1
    
    def __get__(self):
        return f"nombre= {self.__nombre}\npais de origen={self.__paisOrigen}\npais de destino={self.__paisDestino}\nnro de pasajeros={self.__nroPasajeros}\n{self.__pasajeros}"

    def __eq__(self, O):
        suma_total = 0
        for i in range(len(self.__pasajeros)):
            suma_total+=self.__pasajeros[i][3]
        return suma_total
    
    
    def __add__(self, O):
        if(self.__nroPasajeros == O.__nroPasajeros):
            return True
        else:
            return False
    def __sub__(self, O):
        cont_hombres=0
        cont_mujeres = 0
        for i in range(len(self.__pasajeros)):
            if(self.__pasajeros[i][2]=="M"):
                cont_hombres+=1
            else:
                cont_mujeres+=1
        return ["Hombres: ", str(cont_hombres), "Mujeres: ", str(cont_mujeres)]
    

class Pasajero:
    def __init__(self, nomb, edad, genero, costo_pasaje, nro_habitacion):
        self.__nombre = nomb
        self.__edad = edad
        self.__genero = genero
        self.__costo_pasaje = costo_pasaje
        self.__nro_habitacion = nro_habitacion

    # leer datos
    def __set__(self, nuevo_nombre, nueva_edad, nuevo_genero, n_costo_pasaje, n_nro_habitacion):
        self.__nombre = nuevo_nombre
        self.__edad = nueva_edad
        self.__genero = nuevo_genero
        self.__costo_pasaje = n_costo_pasaje
        self.__nro_habitacion = n_nro_habitacion
    
    # mostrar los datos
    def __get__(self):
        return [self.__nombre, str(self.__edad), self.__genero, self.__costo_pasaje, self.__nro_habitacion]
    
    

crucero1 = Crucero("Titanic", "Rusia", "Bolivia", 1, [["Jhon Brand", 43, "M", 5500, 1000]])

crucero2 = Crucero("Titan", "Chile", "Mexico", 1, [["Elvis Yao", 12, "M", 400, 1500]])

pasajero1 = Pasajero("Juan Vargas", 23, "M", 200, 600)
pasajero2 = Pasajero("Martina Vazquez", 79, "F", 63, 10)
pasajero3 = Pasajero("Wilmer Montero", 24, "M", 401, 92)
pasajero4 = Pasajero("Juana Barrera", 30, "F", 400, 1500)
pasajero5 = Pasajero("Martin Figuero", 12, "M", 6003, 1000)

print(crucero1.__get__(), "\n")
print(crucero2.__get__(), "\n")

print("\ningresando pasajeros....\n")

crucero1.__set__(pasajero1)
crucero1.__set__(pasajero2)

crucero2.__set__(pasajero3)
crucero2.__set__(pasajero4)

crucero2.__set__(pasajero5)

print("\nterminado.\n")

print(crucero1.__get__(), "\n")
print(crucero2.__get__(), "\n")

print(f"Suma total del costo de los pasajes= {crucero1==crucero1} - CRUCERO1")
print(f"Suma total del costo de los pasajes= {crucero2==crucero2} - CRUCERO2")

valor = crucero1+crucero2
print("Verificar la cantidad de pasajeros en cada crucero")
if(valor):
    print("Tienen mismo numero de pasajeros")
else:
    print("Tienen diferente numero de pasajeros")


print(f"{crucero1-crucero1} - CRUCERO1")
print(f"{crucero2-crucero2} - CRUCERO2")


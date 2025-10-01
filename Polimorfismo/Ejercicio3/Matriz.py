"""
    Ejercicio 3. Sea la clase Matriz(float matriz[10][10])
a) Implementar un constructor para instanciar un objeto con valores
predeterminados(matriz identidad)
b) Implementar un constructor para Instanciar un objeto matriz
c) Implementar los metodos para sumar(Matriz matriz) y restar(Matriz matriz)
d) Implementar un método igual(Matriz matriz
"""

class Matriz:
    def __init__(self, *args):
        if len(args) == 0:
            self.matriz = [
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0],
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0],
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0, 0, 0, 0],
                [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0, 0, 0, 0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0, 0, 0, 0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0, 0, 0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 1, 0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 1],
            ]
        elif len(args) == 1:
            self.matriz = args[0]
        else:
            self.matriz = args[0]
            self.filas = args[1]
            self.columnas = args[2]

    def __add__(self, O):
        matrizNueva = []
        if (
            len(self.matriz) == 10
            and len(self.matriz[0]) == 10
            and len(O.matriz) == 10
            and len(O.matriz[0]) == 10
        ):
            for i in range(0, len(self.matriz)):
                vector = []
                for j in range(0, len(self.matriz[0])):
                    vector.append(self.matriz[i][j] + O.matriz[i][j])
                matrizNueva.append(vector)
            return Matriz(matrizNueva)
        else:
            return Matriz([])

    def __sub__(self, O):
        if (
            len(self.matriz) == 10
            and len(self.matriz[0]) == 10
            and len(O.matriz) == 10
            and len(O.matriz[0]) == 10
        ):
            matrizNueva = []
            for i in range(0, len(self.matriz)):
                vector = []
                for j in range(0, len(self.matriz[0])):
                    vector.append(self.matriz[i][j] - O.matriz[i][j])
                matrizNueva.append(vector)

            return Matriz(matrizNueva)
        else:
            return Matriz([])

    def __eq__(self, O):
        if (
            len(self.matriz) == 10
            and len(self.matriz[0]) == 10
            and len(O.matriz) == 10
            and len(O.matriz[0]) == 10
        ):
            matrizNueva = []
            for i in range(0, len(self.matriz)):
                vector = []
                for j in range(0, len(self.matriz[0])):
                    if self.matriz[i][j] != O.matriz[i][j]:
                        return False
            return True
        else:
            return False

    def getMatriz(self):
        return self.matriz

    def __str__(self):
        M = ""
        for i in range(0, len(self.matriz)):
            M += "[ "
            for j in range(0, len(self.matriz[0])):
                M += str(self.matriz[i][j]) + " "
            M += "]\n"
        return M


matriz2 = [
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
]

matriz3 = [
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
    [1.2, 3.2, 0, 1.0, 0.0, 0.0, 1.1, 2.2, 5.2, 10.8],
]


m1 = Matriz()
m2 = Matriz(matriz2, 3, 3)
m3 = Matriz(matriz3, 3, 3)

print("Suma de matrices")
print(m2.__add__(m3).__str__())
print("Resta de matrices")
print(m2.__sub__(m2).__str__())
print("Igualdad de matrices")
if m2.__eq__(m3):
    print("Son iguales")
else:
    print("No son iguales")

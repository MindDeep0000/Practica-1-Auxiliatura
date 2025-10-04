class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("Desplazarse...")

    def __str__(self):
        return f"{self.name} {self.age}"
    
class Canguro(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print("Canguro saltar de cuatro patas")
class Leon(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print("leon camina de 4 patas")
class Pinguino(Animal):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print("Pinguino camina de dos patas y nada")
animals = [Leon("Alex", 10), Pinguino("Kriko", 5), Canguro("Jack", 8)]

for animal in animals:
    print(animal)
    animal.desplazarse()
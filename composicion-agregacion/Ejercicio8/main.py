from Fraternidades import Fraternidad
from Bailarines import Bailarin
from Facultades import Facultad
b1 = Bailarin("Juan", 24, "masculino")
b2 = Bailarin("Jose", 21, "masculino")
b3 = Bailarin("Marco", 18, "masculino")
b4 = Bailarin("Josefa", 20, "femenino")
b5 = Bailarin("Albertina", 22, "femenino")
b6 = Bailarin("Miriam", 14, "femenino")


f1 = Facultad("Ciencias", 5)
f2 = Facultad("tecnologia", 6)

fr1 = Fraternidad("Miguel Osco", "Tobas")
fr2 = Fraternidad("Juan Marco Villalba", "tinkus")

fr1.agregarIntegrante(b1, f1, fr1)
fr1.agregarIntegrante(b2, f1, fr1)
fr1.agregarIntegrante(b3, f1, fr1)
fr1.agregarIntegrante(b6, f1, fr1)

fr2.agregarIntegrante(b4, f2, fr2)
fr2.agregarIntegrante(b5, f2, fr2)
fr2.agregarIntegrante(b3, f2, fr2)

print("fraternidad 1")
fr1.verFraternidad()
fr1.edadesIntegrantes()
fr1.verEncargados()

print("fraternidad 2")
fr2.verFraternidad()
fr2.edadesIntegrantes()
fr2.verEncargados()

fr1.mismosParticipantes(fr2)

print("fraternidad 1")
fr1.verFraternidad()
print("fraternidad 2")
fr2.verFraternidad()
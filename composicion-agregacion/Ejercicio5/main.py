""""
    Metodo pricipal
"""

from Universidad import universidad
from Estudiante import estudiante
from Carrera import carrera
# nombre, direccion, nomFacultad, nroCarreras

u1 = universidad("UMSA", "avenida 6 de agosto, plaza del estudiante")
u2 = universidad("UPB", "Achocalla caminop a mallaza")
# estudiantes para la universidad 1
e1 = estudiante("joel", "Barrera", "Quispe", 15285817, 18, 1885980, 123)
e2 = estudiante("Ana", "Valencia", "Velazco", 34526182, 20, 18543262, 627)
e3 = estudiante("Carlos", "Bravo", "Quiroga", 87318374, 12, 16243261, 864)
e4 = estudiante("Jose", "Martinez", "Perati", 73287612, 81, 59274183, 879)
# estudiantes para la universidad 2
e5 = estudiante("diego", "Barrera", "Quispe", 15285817, 18, 1885980, 123)
e6 = estudiante("Ana", "Valencia", "Velazco", 34526182, 20, 18543262, 627)
e7 = estudiante("Carlos", "Bravo", "Quiroga", 87318374, 12, 16243261, 864)

u1.modificar_facultad1("Ingenieria", 3)
u1.agregar_carrera1_facultad1("mecanica")
u1.agregar_carrera2_facultad1("electronica")
u1.agregar_carrera3_facultad1("quimica")

u2.modificar_facultad1("Tecnologia", 3)
u2.agregar_carrera1_facultad1("aeronautica")
u2.agregar_carrera2_facultad1("desarrollo")


u1.agregarEstudiante_carrera1_facultad1(e1)
u1.agregarEstudiante_carrera1_facultad1(e2)
u1.agregarEstudiante_carrera2_facultad1(e3)
u1.agregarEstudiante_carrera3_facultad1(e4)

u2.agregarEstudiante_carrera1_facultad1(e5)
u2.agregarEstudiante_carrera2_facultad1(e6)
u2.agregarEstudiante_carrera2_facultad1(e7)

u1.contarEstudiantes()
u2.contarEstudiantes()

print(u1.buscar_estudiante(123))
print(u2.buscar_estudiante(87318874))

u1.cambiarCarrera("mecanica", "electronica", e1, "Ingenieria")
u1.contarEstudiantes()



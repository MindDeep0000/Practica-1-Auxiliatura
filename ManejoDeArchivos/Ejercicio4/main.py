from estudiante import Estudiante
from nota import Nota
from archinota import ArchiNota


def imprimir_notas(notas):
    if not notas:
        print("(sin notas)")
        return
    for n in notas:
        print(n)


def demo():
    gestor = ArchiNota()
    gestor.crear_archivo()

    # Crear estudiantes
    s1 = Estudiante(1, "Ana", "Perez", "Gomez", 20)
    s2 = Estudiante(2, "Luis", "Garcia", "Diaz", 21)
    s3 = Estudiante(3, "Maria", "Lopez", "Soto", 19)

    # Agregar estudiantes con nota por defecto en materia Matematica
    gestor.agregar_estudiantes([s1, s2, s3], materia="Matematica", nota_default=0.0)

    # Añadir/actualizar notas concretas
    notas_actuales = gestor.leer_notas()
    # modificar algunas
    for n in notas_actuales:
        if n.estudiante.ru == 1 and n.materia == "Matematica":
            n.nota_final = 15.5
        if n.estudiante.ru == 2 and n.materia == "Matematica":
            n.nota_final = 18.0
        if n.estudiante.ru == 3 and n.materia == "Matematica":
            n.nota_final = 18.0

    # Guardar actualizadas
    gestor.guardar_notas(notas_actuales)

    print("Todas las notas:")
    imprimir_notas(gestor.leer_notas())

    prom = gestor.promedio_total()
    print(f"\nPromedio total de notas: {prom:.2f}" if prom is not None else "No hay notas")

    top = gestor.mejores()
    print("\nMejor(es) estudiante(s):")
    imprimir_notas(top)

    print("\nOrdenados por Matematica (desc):")
    imprimir_notas(gestor.ordenar_por_materia("Matematica"))


if __name__ == "__main__":
    demo()

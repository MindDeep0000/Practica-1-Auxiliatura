from ArchRefri import ArchRefri
from Alimento import Alimento

def main():
    refri = ArchRefri("Mi Refri")

    # Crear alimentos (se guardan automáticamente en JSON)
    refri.crear(Alimento("Leche", "2025-01-10", 2))
    refri.crear(Alimento("Queso", "2024-12-01", 1))
    refri.crear(Alimento("Huevos", "2024-10-20", 0))

    print("\n--- Todos ---")
    refri.mostrar_todos()

    print("\n--- Modificar Leche ---")
    refri.modificar_por_nombre("Leche", "2025-02-01", 5)
    refri.mostrar_todos()

    print("\n--- Caducados antes de 2025-01-01 ---")
    refri.mostrar_caducados_antes_de("2025-01-01")

    print("\n--- Eliminar cantidad 0 ---")
    refri.eliminar_cantidad_cero()
    refri.mostrar_todos()

    print("\n--- Vencidos al 2024-12-05 ---")
    refri.mostrar_vencidos("2024-12-05")

    print("\n--- Mayor cantidad ---")
    refri.mostrar_mayor_cantidad()

if __name__ == "__main__":
    main()

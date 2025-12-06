from gestor import GestorCharangos
from charango import Charango

gestor = GestorCharangos("Ejercicio1/charangos.json")
gestor.cargar()

# Ejemplos de charangos
c1 = Charango("Madera", 10, [True]*10)
c2 = Charango("Fibra", 8, [True, False, False, True, True, False, True, False])
c3 = Charango("Aluminio", 10, [False]*10)

# Guardamos los charangos iniciales
gestor.charangos = [c1, c2, c3]
gestor.guardar()

# Aplicar los métodos
gestor.eliminar_con_muchas_cuerdas_false()  # b)
gestor.guardar()

# Ejemplo de uso extra:
print("Charangos de material Madera:")
for c in gestor.listar_por_material("Madera"):
    print(c.to_dict())

print("Charangos con 10 cuerdas:")
for c in gestor.buscar_con_diez_cuerdas():
    print(c.to_dict())

gestor.ordenar_por_material()
gestor.guardar()

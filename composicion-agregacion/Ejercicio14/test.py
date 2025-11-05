from Empleado import Empleado
from Empresa import Empresa
# crear la empresa
emp1 = Empresa("Tecnología Innova S.A. de C.V.")
# crear los empleados
e1 = Empleado("Ana Martínez", "Ingeniera de Software", 8500000)
e2 = Empleado("Carlos Gómez", "Especialista en Seguridad Informática", 7200000)
e3 = Empleado("Lucía Fernández", "Analista de Datos", 6800000)
# agregar los empleados a la empresa 1
emp1.addEmpleado(e1)
emp1.addEmpleado(e2)
emp1.addEmpleado(e3)

# crear la empresa
emp2 = Empresa("Servicios Logísticos del Sur S.R.L.")
# crear los empleados
e4 = Empleado("Javier Rojas", "Gerente de Operaciones", 9100000)
e5 = Empleado("Sofía Díaz", "Coordinadora de Almacén", 5900000)
e6 = Empleado("Mateo López", "Repartidor", 4300000)
#agregar empleados a la empresa 2
emp2.addEmpleado(e4)
emp2.addEmpleado(e5)
emp2.addEmpleado(e6)

# mostrar informacion de la empresa
print("* * * informacion acerca de las empresa")
emp1.infoEmpresa()
emp2.infoEmpresa()
print("* * * * * * * * * * * * * * * * * * * *")

# buscar empleado
print("* * * buscar empleados")
emp1.buscarEmp("Ana")
emp2.buscarEmp("Lucia")
print("* * * * * * * * * * * * * * * * * * * *")
# eliminar empleado
emp2.eliminarEmp("Mater")

# promedio de salarios en ambas empresa
prd1 = emp1.promedioSalarios()
prd2 = emp2.promedioSalarios()
print(f"\npromedio de salario de la empresa 1 {prd1}")
print(f"promedio de salario de la empresa 2 {prd2}\n")

# empleados con mayor salario de 9000000
print("* * * empleados con mayor salario")
empresa = [emp1, emp2]
for e in empresa:
    e.salarioMayor(9000000)
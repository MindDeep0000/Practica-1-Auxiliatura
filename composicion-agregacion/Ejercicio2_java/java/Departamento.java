import java.util.ArrayList;
import java.util.List;

public class Departamento {
    private String nombre;
    private String area;
    private List<Empleado> listaEmpleados;

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.listaEmpleados = new ArrayList<>();
    }

    public void mostrarEmpleados() {
        for (Empleado empleado : listaEmpleados) {
            if (empleado != null) {
                System.out.println(empleado);
            }
        }
    }

    public void cambioSalario(String nombre, double nuevoSalario) {
        for (Empleado emp : listaEmpleados) {
            if (emp.getNombre().equals(nombre)) {
                System.out.println("El empleado: ");
                System.out.println(emp);
                System.out.println("está cambiando su sueldo a: ");
                emp.setSalario(nuevoSalario);
                System.out.println(emp);
                break;
            }
        }
    }

    public void aniadir(Empleado empleado) {
        listaEmpleados.add(empleado);
    }

    public void eliminar(Empleado empleado) {
        listaEmpleados.remove(empleado);
    }

    public List<Empleado> getListaEmps() {
        return listaEmpleados;
    }

    public void verificarMismoDepartamento(Departamento dep) {
        boolean bandera = false;
        List<Empleado> lista = dep.getListaEmps();
        for (Empleado A : listaEmpleados) {
            for (Empleado B : lista) {
                if (A.equals(B)) {
                    System.out.println("coincidencia encontrada con: ");
                    System.out.println(A);
                    listaEmpleados.remove(A);
                    bandera = true;
                }
                if(bandera)
                    break;
            }
            if (bandera)
                break;
        }
    }

    public void cambiarDepartamento(Departamento dep) {
        List<Empleado> lista = this.getListaEmps();
        for (Empleado valor : lista) {
            dep.aniadir(valor);
            this.eliminar(valor);
        }
    }
}

public class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }

    public double getSalario() {
        return this.sueldo;
    }

    public void setSalario(double nuevoSueldo) {
        this.sueldo = nuevoSueldo;
    }

    public String getCargo() {
        return this.cargo;
    }

    public String getNombre() {
        return this.nombre;
    }

    @Override
    public String toString() {
        return "nombre: " + this.getNombre() + " cargo: " + this.getCargo() + " sueldo: " + this.getSalario();
    }
}

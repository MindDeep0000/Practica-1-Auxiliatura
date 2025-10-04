package Ejercicio_13;

public class Administrativo extends Empleado{
    private String cargo;

    public Administrativo(String cargo, String nombre, int sueldoMes) {
        super(nombre, sueldoMes);
        
        this.cargo = cargo;
    }

    @Override
    public String toString() {
        return "Administrativo{" + "cargo=" + cargo + '}';
    }
    
}

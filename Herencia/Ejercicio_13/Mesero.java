package Ejercicio_13;

/**
 *
 * @author ACCESO
 */
public class Mesero extends Empleado{
    private double propina;
    private int horasExtra;
    private float sueldoHora;

    public Mesero(double propina, int horasExtra, float sueldoHora, String nombre, int sueldoMes) {
        super(nombre, sueldoMes);
        this.propina = propina;
        this.horasExtra = horasExtra;
        this.sueldoHora = sueldoHora;
    }
    
    public double getPropina(){
        return this.propina;
    }
    
}

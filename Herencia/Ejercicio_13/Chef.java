package Ejercicio_13;

/**
 *
 * @author ACCESO
 */
public class Chef extends Empleado{
    private int horasExtra;
    private String tipo;
    private float sueldoHora;

    public Chef(int horasExtra, String tipo, float sueldoHora, String nombre, int sueldoMes) {
        super(nombre, sueldoMes);
        this.horasExtra = horasExtra;
        this.tipo = tipo;
        this.sueldoHora = sueldoHora;
    }
    
    public double sueldoTotal(int v){
        return horasExtra*sueldoHora;
    }
    
}

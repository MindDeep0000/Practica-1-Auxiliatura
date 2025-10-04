package Ejercicio_11;

/**
 *
 * @author ACCESO
 */
public class Empleado{
    private String ocupacion;
    private int aniosExp;

    public Empleado(String ocupacion, int aniosExp) {
        this.ocupacion = ocupacion;
        this.aniosExp = aniosExp;
    }

    public String getOcupacion() {
        return ocupacion;
    }

    public int getAniosExp() {
        return aniosExp;
    }
    
    
}

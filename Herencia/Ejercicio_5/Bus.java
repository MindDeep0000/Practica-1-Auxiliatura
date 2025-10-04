package Ejercicio_5;

/**
 *
 * @author ACCESO
 */
public class Bus extends Vehiculo{
    private int capacidad;
    private String sindicato;

    public Bus(int capacidad, String sindicato, String conductor, String placa, int id) {
        super(conductor, placa, id);
        this.capacidad = capacidad;
        this.sindicato = sindicato;
    }
    
    
    
}

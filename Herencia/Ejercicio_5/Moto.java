package Ejercicio_5;

/**
 *
 * @author ACCESO
 */
public class Moto extends Vehiculo{
    private int cilindrada;
    private boolean casco;

    public Moto(int cilindrada, boolean casco, String conductor, String placa, int id) {
        super(conductor, placa, id);
        this.cilindrada = cilindrada;
        this.casco = casco;
    }
    
    
}

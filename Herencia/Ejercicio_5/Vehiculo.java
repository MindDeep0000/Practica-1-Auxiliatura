package Ejercicio_5;

/**
 *
 * @author ACCESO
 */
public class Vehiculo {
    protected String conductor, placa;
    protected int id;

    public Vehiculo(String conductor, String placa, int id) {
        this.conductor = conductor;
        this.placa = placa;
        this.id = id;
    }
    
    @Override
    public String toString(){
        return String.format("%s %s", this.conductor, this.placa);
    }
    
    public void cambiarConductor(String conductor){
        this.conductor = conductor;
    }
}

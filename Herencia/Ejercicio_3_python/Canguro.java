package Ejercicio_3;

/**
 *
 * @author ACCESO
 */
public class Canguro extends Animal{

    public Canguro(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void desplazarse(){
        System.out.println("Canguro saltar de cuatro patas");
    }
}

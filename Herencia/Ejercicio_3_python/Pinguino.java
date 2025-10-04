package Ejercicio_3;

/**
 *
 * @author ACCESO
 */
public class Pinguino extends Animal{

    public Pinguino(String nombre, int edad) {
        super(nombre, edad);
    }
    
    @Override
    public void desplazarse(){
        System.out.println("Pinguino camina de dos patas y nada");
    }
}

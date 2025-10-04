package Ejercicio_3;

/**
 *
 * @author ACCESO
 */
public class Leon extends Animal{

    public Leon(String nombre, int edad) {
        super(nombre, edad);
    }
    @Override
    public void desplazarse(){
        System.out.println("leon camina de 4 patas");
    }
    
    
}

package Ejercicio_3;

/**
 *
 * @author ACCESO
 */
public class Animal {
    private String nombre;
    private int edad;

    public Animal(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    public void desplazarse(){
        System.out.println("Desplazarse...");
    }
    @Override
    public String toString(){
        return String.format("%s %d", this.nombre, this.edad);
    }
}

package Ejercicio_11;

/**
 *
 * @author ACCESO
 */
public class Persona {
    private String nombre;
    private int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
    
    public String mostrarPersona(){
        return String.format("nombre=%s edad=%d", this.nombre, this.edad);
    }
    public String getNombre(){
        return this.nombre;
    }
}

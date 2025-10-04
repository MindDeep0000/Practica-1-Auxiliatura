
package Ejercicio5;

/**
 * Ejercicio 5. Define la clase Persona (nombre, paterno, materno, edad, ci)
 * a) Instanciar a dos personas.
 * b) Implementar método mostrarDatos().
 * c) Implementar el metodo mayorDeEdad() que determina si la persona es mayor de edad o no.
 * d) Implementar método modificarEdad(nuevo) que modifica la edad de la persona.
 * e) Verificar si las dos personas tienen el mismo apellido paterno.
 */

public class Persona {
    private String nombre, paterno, materno;
    private int edad;
    private long ci;
    
    public Persona(String nombre, String paterno, String materno, int edad, long ci){
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }
    
    public String mostrarDatos(){
        return String.format("nombre completo: %s %s %s edad: %d c.i.: %d", this.nombre, this.paterno, this.materno, this.edad, this.ci);
    }
    
    public String mayorDeEdad(){
        if(this.edad>=18){
            return this.nombre + " es mayor de edad";
        }
        return this.nombre + " no es mayor de edad";
    }
    
    public void modificaredad(int nuevo){
        this.edad = nuevo;
    }
    
    public String tocayo(Persona nueva){
        if(this.paterno.equals(nueva.paterno)){
            return "Comparten el mismo apellido";
        }
        return "No comparten similitud en los apellidos";
    }
    
}

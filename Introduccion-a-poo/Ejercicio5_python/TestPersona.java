package Ejercicio5;

/**
 * Ejercicio 5. Define la clase Persona (nombre, paterno, materno, edad, ci)
 * a) Instanciar a dos personas.
 * b) Implementar método mostrarDatos().
 * c) Implementar el metodo mayorDeEdad() que determina si la persona es mayor de edad o no.
 * d) Implementar método modificarEdad(nuevo) que modifica la edad de la persona.
 * e) Verificar si las dos personas tienen el mismo apellido paterno.
 */

public class TestPersona {
    public static void main(String[] args) {
        Persona p1 = new Persona("Jordi", "Andrade", "Gotret", 35, 12781234);
        Persona p2 = new Persona("Mary", "Andrade", "Arabi", 18, 34129090);
        
        System.out.println(p1.mostrarDatos());
        System.out.println(p2.mostrarDatos());
        
        System.out.println(p1.mayorDeEdad());
        System.out.println(p2.mayorDeEdad());
        
        System.out.println("Modificando la edad de jordi");
        p1.modificaredad(32);
        System.out.println(p1.mostrarDatos());
        
        
        System.out.println(p1.tocayo(p2));
    }
}

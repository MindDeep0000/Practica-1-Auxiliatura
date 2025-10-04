/**
 * Define las clases: Persona {#nombre #paterno #materno #edad}
 * Esudiante {-ru -matricula}
 * Docente {-sueldo -regProfesional}
 * a) Instanciar a dos estudiantes.y un docente.
 * b) Implementar el método mostrar() en las 3 clases.
 * c) Agregar el método promedio() que devuelva el promedio de la edad de los
 * esdiantes.
 * d) Implementar el método modificarEdad() para el estudiante.
 * e) Verificar si uno de los estudiantes tiene la misma edad que el docente.
 */
package Ejercicio_7;

/**
 *
 * @author ACCESO
 */
public class App {
    public static void main(String[] args) {
        GrupoDeEstudiantes g1 = new GrupoDeEstudiantes();
        
        Estudiante d1 = new Estudiante(1234120, 123, "Jose", "Mendoza", "Quispe", 24);
        Estudiante d2 = new Estudiante(1223913, 432, "Alex", "Mamani", "Mamani", 18);
        Estudiante d3 = new Estudiante(5917304, 183, "German", "Achu", "Bueno", 12);
        
        g1.agregarEstudiante(d1);
        g1.agregarEstudiante(d2);
        g1.agregarEstudiante(d3);
        
        Docente mate = new Docente(12.000, 1251, "Mario", "Ruiz", "Olivera", 56);
        
        System.out.println(d1.toString());
        System.out.println(d2.toString());
        System.out.println(d3.toString());
        System.out.println(mate.toString());
        System.out.println("Promedio de edades: " + g1.promedio());
        
        d2.setEdad(30);
        
        System.out.println(d2.toString());
        
        System.out.println("Promedio de edades: " + g1.promedio());
        if(d1.mismaEdad(mate))
            System.out.println("Tienen la misma edad");
        else
            System.out.println("No tienen la misma edad");
        
    }
}

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
import java.time.LocalDateTime;
/**
 *
 * @author ACCESO
 */
public class Docente extends Persona{
    private LocalDateTime fechaCreacion;
    private double sueldo;
    private int nroRegistroProfesional;
    
    public Docente(double sueldo, int nroRegistroProfesional, String nombre, String paterno, String materno, int edad){
        super(nombre, paterno, materno, edad);
        this.sueldo = sueldo;
        this.nroRegistroProfesional = nroRegistroProfesional;
        this.fechaCreacion = LocalDateTime.now();
    }    

    @Override
    public String toString() {
        return "Docente{" + "sueldo=" + sueldo + ", nroRegistroProfesional=" + nroRegistroProfesional +"Fecha= "+this.fechaCreacion+'}';
    }
    
}

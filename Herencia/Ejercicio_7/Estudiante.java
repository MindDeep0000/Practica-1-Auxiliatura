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
 * @author ACCESO
 */
import java.util.ArrayList;
public class Estudiante extends Persona {

    private int ru, matricula;

    public Estudiante(int ru, int matricula, String nombre, String paterno, String materno, int edad) {
        super(nombre, paterno, materno, edad);
        this.ru = ru;
        this.matricula = matricula;
    }

    @Override
    public String toString() {
        return "Estudiante{" + "ru=" + ru + ", matricula=" + matricula +" edad="+edad+'}';
    }

    @Override
    public void setEdad(int edad) {
        this.edad = edad;
    }

    public boolean mismaEdad(Docente d) {
        if (this.getEdad() == d.getEdad()) {
            return true;
        }
        return false;
    }
}

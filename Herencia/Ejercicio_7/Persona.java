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
public class Persona {

    protected String nombre, paterno, materno;
    protected int edad;

    public Persona(String nombre, String paterno, String materno, int edad) {
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", paterno=" + paterno + ", materno=" + materno + ", edad=" + edad + '}';
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

}

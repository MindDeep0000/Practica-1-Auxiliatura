/**
 * Sea la clase político(profesión, añosExp) y la clase Partido(nombreP,rol)
 * crear la clase presidente(nombre, apellido) que sea una clase hija de Político y Partido
 * a) Diseñar el diagrama de clases
 * b) Instanciar de dos formas diferentes a un presidente
 * c) Crear un vector de presidente con minimo 3 presidentes y buscar al presidente de
 * nombre x y mostrar el partido politico y la profesión.
 */
package Ejercicio_9;

/**
 *
 * @author ACCESO
 */
public class Partido {
    private String nombre, rol;

    public Partido(String nombre, String rol) {
        this.nombre = nombre;
        this.rol = rol;
    }

    public Partido(String nombre) {
        this.nombre = nombre;
    }
    
    
    
}

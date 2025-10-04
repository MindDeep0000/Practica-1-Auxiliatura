/**
 * Ejercicio 1. Dado el siguiente diagrama
 *
 * a) Corrija los errores que tiene el diagrama.
 * b) Implemente el diagrama una vez corregido.
 * c) Haga una lista de los errores
 * cometidos y de cómo evitarlos.
 */
package Ejercicio_1;

/**
 *
 * @author Joel Barrera Quispe
 */
public class Jefe extends Persona{
    private String sucursal, CI, tipo;

    public Jefe(String sucursal, String CI, String tipo, String nombre, String apellido) {
        super(nombre, apellido, CI);
        this.sucursal = sucursal;
        this.CI = CI;
        this.tipo = tipo;
    }
    
    @Override
    public void method(){
        System.out.println("Guiar a su personal");
    }
}

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
public class Cliente extends Persona{
    private String nroCompra, idCliente, nombre;

    public Cliente(String nroCompra, String idCliente, String nombre, String apellido, String CI) {
        super(nombre, apellido, CI);
        this.nroCompra = nroCompra;
        this.idCliente = idCliente;
        this.nombre = nombre;
    }
    
    @Override
    public void method(){
        System.out.println("Comprar");
    }
}

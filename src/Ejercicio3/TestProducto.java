
/**
 * Ejercicio 3. Diseña una clase Producto que tenga atributos nombre, precio y
 * stock. Agrega métodos para vender productos y reabastecer el stock.
 * a) Define la clase y los atributos.
 * b) Agrega un método vender(cantidad: Int) que reste del stock
 * c) Agrega un método reabastecer(cantidad: Int) que sume al stock.
 */

package Ejercicio3;

/**
 *
 * @author Joel Barrera Quispe Inf 121
 * Aux. Cristian Alvarez
 */
public class TestProducto {
    public static void main(String[] args){
        Producto zapatos = new Producto("Zapatos", 128.34, 100);
        zapatos.vender(45);
        System.out.println(zapatos.toString());
        zapatos.reabastecer(14);
        System.out.println(zapatos.toString());
    }
}

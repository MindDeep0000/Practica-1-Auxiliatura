package Ejercicio3;

/**
 * Joel Barrera Quispe
 */

public class TestProducto {
    public static void main(String[] args){
        Producto zapatos = new Producto("Zapatos", 128.34, 100);
        System.out.println(zapatos.toString());
        zapatos.vender(45);
        System.out.println("Se venden 45 unidades \n" + zapatos.toString());
        zapatos.reabastecer(14);
        System.out.println("Se reabastecen 14 unidades \n" + zapatos.toString());
    }
}

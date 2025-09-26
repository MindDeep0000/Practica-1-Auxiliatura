package Ejercicio3;

/**
 *
 * @author ACCESO
 */
public class Producto {
    private String nombre;
    private double precio;
    private int stock;
    
    public Producto(String nombre, double precio, int stock){
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
    
    public void vender(int cantidad){
        this.stock -=cantidad;
    }
    
    public void reabastecer(int cantidad){
        this.stock+=cantidad;
    }
    
    public String toString(){
        return "nombre: " + this.nombre + " precio: " + this.precio+" stock: "+this.stock;
    }
}

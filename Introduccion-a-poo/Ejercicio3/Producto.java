package Ejercicio3;

/**
 * Ejercicio 3. Diseña una clase Producto que tenga atributos nombre, precio y
 * stock. Agrega métodos para vender productos y reabastecer el stock.
 * a) Define la clase y los atributos.
 * b) Agrega un método vender(cantidad: Int) que reste del stock
 * c) Agrega un método reabastecer(cantidad: Int) que sume al stock.
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

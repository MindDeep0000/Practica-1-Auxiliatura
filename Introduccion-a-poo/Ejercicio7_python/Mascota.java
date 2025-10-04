/**
 * Ejercicio 7. Dada la clase Mascota.
 * --------------------
 * |    Mascota       |
 * --------------------
 * | - nombre: String |
 * | - tipo: String   |
 * | - energia: int   |
 * --------------------
 * 
 * a) Agrega un método para alimentar (+20 de energía, máximo 100).
 * b) Agrega un método para jugar (-15 de energía, mínimo 0).c) Crea dos mascotas, aliméntalas y hazlas jugar, mostrando su energía en cada
 * paso.
 */
package Ejercicio7;

/**
 *
 * @author Joel Barrera Quispe inf 121 E
 * Aux. Cristian Alvarez
 */
public class Mascota {
    private String nombre, tipo;
    private int energia;
    
    public Mascota(String nombre, String tipo, int energia){
        this.nombre = nombre;
        this.tipo = tipo;
        this.energia = energia;
    }
    
    public void alimentar(int masEnergia, int maximo){
        int aux = this.energia + masEnergia;
        if(aux>maximo){
            System.out.println("tu mascota esta con demasiada energia");
        }else{
            this.energia +=masEnergia;
        }
        
    }
    
    public void jugar(int menosEnergia, int minimo){
        int resta = this.energia - menosEnergia;
        if(resta<minimo){
            System.out.println("Tu mascota ya esta mu canasada, dejala descanzar");
        }else{
            this.energia -=menosEnergia;
        }
    }
    
    public String estadoActual(){
        return String.format("nombre: %s, tipo: %s, energia: %d (percent)", this.nombre, this.tipo, this.energia);
    }
}
/**
 * tener cuidado al declara varivales locales porque afectana toda la clase
 */
/**
 * Realiza la abstracción de un Bus.
 * a) Al bus desean subir X cantidad de pasajeros, actualiza los datos del bus.
 * b) Crea un método para cobrar pasaje a los pasajeros. (Costo del pasaje: bs. 1.50)’
 * c) Muestra cuántos asientos quedan disponibles.
 * d) Crea una instancia del bus y utiliza los métodos de los incisos anteriores.
 */
package Ejercicio2;

/**
 *
 * @author Joel Barrera Quispe INF-121 Aux. Cristian Alvarez
 */
public class Bus {

    private int cant_pasajeros;
    private double dinero_ganado;
    private int cant_asientos;

    public Bus(int cant_asientos) {
        this.cant_asientos = cant_asientos;
        this.dinero_ganado = 0;
        this.cant_pasajeros = 0;
    }

    public void cobrar_pssaje() {
        this.dinero_ganado += 1.50 * this.cant_pasajeros;
        this.cant_asientos -= this.cant_pasajeros;
    }

    public int getCantAsientos() {
        return cant_asientos;
    }

    public int getCant_pasajeros() {
        return cant_pasajeros;
    }

    public void setCant_pasajeros(int cant_pasajeros) {
        this.cant_pasajeros = +cant_pasajeros;
    }

    public String toString() {
        return "dinero ganado " + this.dinero_ganado;
    }
}

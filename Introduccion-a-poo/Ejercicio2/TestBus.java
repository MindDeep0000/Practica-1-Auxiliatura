package Ejercicio2;

/**
 *
 * @author Joel Barrera Quispe INF-121 Aux. Cristian Alvarez
 *
 */
/**
 * EJERCICIO 2 Realiza la abstracción de un Bus. a) Al bus desean subir X
 * cantidad de pasajeros, actualiza los datos del bus. b) Crea un método para
 * cobrar pasaje a los pasajeros. (Costo del pasaje: bs. 1.50)’ c) Muestra
 * cuántos asientos quedan disponibles. d) Crea una instancia del bus y utiliza
 * los métodos de los incisos anteriores.
 */
public class TestBus {

    public static void main(String[] args) {
        Bus Kriko = new Bus(30); //cant_asientos
        Kriko.setCant_pasajeros(20); // cantidad de pasasjeros que van a ingresar al bus
        System.out.println("Han ingresado 20 pasajeros");
        Kriko.cobrar_pssaje(); // cobrar pasaje a los pasajeros
        System.out.println("cantidad de asientos disponibles: " + Kriko.getCantAsientos());
        System.out.println(Kriko.toString());

    }
}

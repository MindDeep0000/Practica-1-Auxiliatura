package Ejercicio2;

/**
 *
 * @author Joel Barrera Quispe INF-121 Aux. Cristian Alvarez
 *
 */
public class TestBus {

    public static void main(String[] args) {
        Bus Kriko = new Bus(30); //cant_asientos
        Kriko.setCant_pasajeros(20);
        Kriko.cobrar_pssaje();
        System.out.println("cantidad de asientos disponibles: " + Kriko.getCantAsientos());
        System.out.println(Kriko.toString());

    }
}

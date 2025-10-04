/**
 * Vehiculo {#conductor #placa #id}
 * Bus {-capacidad -sindicato}
 * Auto {-caballosFuerza -descapotable}
 * Moto {-cilindrada -casco}
 * a) Instanciar un vehículo de cada tipo
 * b) Mostrar La placa y conductor cada vehículo.
 * c) Crear un método para cambiar al conductor de un vehículo
 */

package Ejercicio_5;

/**
 *
 * @author ACCESO
 */
public class TestVehiculo {
    public static void main(String[] args) {
        Bus bus1 = new Bus(15, "Bolivar", "Javier Nogales", "123JHRF", 123);
        Auto auto1 = new Auto(30, true, "Crstian Vallejos", "456HFKE", 152);
        Moto moto1 = new Moto(2, true, "Joel Penianieto", "236IJRA", 148);
        
        System.out.println("Bus: "+bus1.toString());
        System.out.println("Auto: "+auto1.toString());
        System.out.println("Moto: "+moto1.toString());
        
        bus1.cambiarConductor("Pepe Poison");
        
        System.out.println("Bus: "+bus1.toString());
    }
}

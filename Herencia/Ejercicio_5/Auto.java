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
public class Auto extends Vehiculo {

    private int caballosFuerza;
    private boolean descapotable;

    public Auto(int caballosFuerza, boolean descapotable, String conductor, String placa, int id) {
        super(conductor, placa, id);
        this.caballosFuerza = caballosFuerza;
        this.descapotable = descapotable;
    }
}

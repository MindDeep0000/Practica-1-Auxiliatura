
package Ejercicio_15;

/**
 *
 * @author ACCESO
 */
public class Ciclista {
    private String tipoBicicleta;

    public Ciclista(String tipoBicicleta) {
        this.tipoBicicleta = tipoBicicleta;
    }
    
    public void pedalear(){
        System.out.println("Pedaleando en bicicleta "+this.tipoBicicleta);
    }
    
}

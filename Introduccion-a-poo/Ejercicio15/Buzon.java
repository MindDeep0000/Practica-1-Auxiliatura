package Ejercicio15;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
/**
 *
 * @author Joel Barrera Quispe
 */

/**
 * 
 * Ejercicio 15.
 * 
 * a) Instanciar 3 buzones diferentes, cada uno con al menos 3 cartas. 
 * b) Instanciar 3 cartas con sus respectivas descripciones. 
 * c) Verificar cuántas cartas recibió el destinatario “X”. 
 * d) Eliminar la carta de la matriz cuyo código sea “X”. 
 * e) Verificar si algún remitente ha recibido alguna carta y,en ese caso, indicar de quién. 
 * f) Buscar una palabra clave (por ejemplo,"amor") en las descripciones de las cartas instanciadas. 
 * g) Por cada coincidencia, mostrar el código, remitente y destinatario correspondientes.
 */


public class Buzon {
    private int nro, nroC;
    private List<List<String>> c = new ArrayList<>();
    
    public Buzon(int nroBuzon, int nroCarta, List c){
        this.nro = nroBuzon;
        this.nroC = nroCarta;
        this.c = c;
    }
    
    public int getnroCartasDeDestinatario(String nombre){
        int cantidad=0;
        for(int i = 0; i < getC().size(); i++){
            if(getC().get(i).get(2).equals(nombre))
                cantidad++;
        }
        System.out.print("El destinatario "+nombre+" recibio un total de: ");
        return cantidad;
    }
    
    public void eliminarCarta(String codigo){
        System.out.print("\neliminando la carta: " + codigo+"\n");
        for(int i=0; i<getC().size(); i++){
            if(c.get(i).get(0).equalsIgnoreCase(codigo)){
                getC().remove(i);
                this.nroC--;
            }
        }
    }
    
    public void mostrarBuzon(){
        System.out.println("\nnumero de buzon: " + this.getNro());
        System.out.println("numero de cartas: "+this.getNroC());
        System.out.println(this.getC());
    }
    
    public void cartaAremitente(){
        System.out.println("");
        for (int i = 0; i < this.c.size(); i++) {
            String remitente = this.c.get(i).get(1);
            for(int j=0; j<this.c.size(); j++){
                if(remitente.equals(this.c.get(j).get(2))){
                    System.out.print("De: "+this.c.get(j).get(1));
                    System.out.println(" Para remitente: "+this.c.get(j).get(2));
                }
            }
        }
    }

    public void buscarCarta(String codigo){
        System.out.println(" la carta: ");
        for (int i = 0; i < c.size(); i++) {
            if(c.get(i).get(0).equals(codigo)){
                System.out.println(c.get(i));
                break;
            }
        }
        
    }
    
    public int getNro() {
        return nro;
    }

    public int getNroC() {
        return nroC;
    }

    public List<List<String>> getC() {
        return c;
    }
}

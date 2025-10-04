package Ejercicio15;

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


public class Carta {
    private String codigo;
    private String descripcion;
    
    
    public Carta(String codigoC, String descripcionC){
        this.codigo = codigoC;
        this.descripcion = descripcionC;
    }
    
    public boolean buscarPalabra(String palabra){
        System.out.print("La palabra: " + palabra+" esta en");
        
        if(this.getDescripcion().contains(palabra)){
            return true;
        }
        return false;
        
    }
    
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getDescripcion() {
        return descripcion;
    }
    
    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }   
}

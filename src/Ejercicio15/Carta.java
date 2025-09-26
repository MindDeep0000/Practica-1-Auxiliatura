package Ejercicio15;

/**
 *
 * @author ACCESO
 */
public class Carta {
    private String codigo;
    private String descripcion;
    
    
    public Carta(String codigoC, String descripcionC){
        this.codigo = codigoC;
        this.descripcion = descripcionC;
    }
    
    public boolean buscarPalabra(String palabra){
        System.out.println("Busqueda de: " + palabra);
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

package Ejercicio_15;

/**
 *
 * @author ACCESO
 */
public class Nadador {
    private String estiloNatacion;
    private int tiempoBajoAgua;
    private boolean aleetas;

    public Nadador(
            String estiloNatacion, 
            int tiempoBajoAgua, 
            boolean aleetas) 
    {
        this.estiloNatacion = estiloNatacion;
        this.tiempoBajoAgua = tiempoBajoAgua;
        this.aleetas = aleetas;
    }

    public String getEstiloNatacion() {
        return estiloNatacion;
    }

    public int getTiempoBajoAgua() {
        return tiempoBajoAgua;
    }

    public boolean isAleetas() {
        return aleetas;
    }
    
    
}

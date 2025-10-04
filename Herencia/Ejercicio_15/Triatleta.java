package Ejercicio_15;

public class Triatleta extends Ciclista implements iCorredor, iNadador{
    private Corredor corredor;
    private Nadador nadador;
    
    public Triatleta(String tipoBicicleta, 
            int distanciaPreferida, 
            String tecnicaPreferida, 
            String estiloNatacion, 
            int tiempoBajoAgua, 
            boolean aletas) 
    {
        super(tipoBicicleta);
        corredor = new Corredor(distanciaPreferida, tecnicaPreferida);
        nadador = new Nadador(estiloNatacion, tiempoBajoAgua, aletas);
    }
    public void correr(){
        System.out.println("Corriendo una distancia de " + corredor.getDistanciaPreferida() + " metros");
    }
    
    public void tecnicas(){
        System.out.println("Tecnica preferida " + corredor.getTecnicaPreferida());
    }
    
    public void nadar(){
        System.out.println("Nadando estilo " + nadador.getEstiloNatacion());
    }
    
    public void nadarDebajoAgua(){
        System.out.println("Permanecer bajo el agua solo " + nadador.getTiempoBajoAgua()+" segundos");
    }
    
    public boolean tieneAletas(){
        return nadador.isAleetas();
    }
}

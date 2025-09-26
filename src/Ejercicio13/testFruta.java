package Ejercicio13;
/**
 *
 * @author ACCESO
 */
public class testFruta {
    public static void main(String[] args) {
        Frutas manzana = new Frutas();        
        Frutas pera = new Frutas("pera", "fruta pomácea", 5, new String[]{"C", "A", "B", "K", "E"}); //String nombre, String tipo, int nroVitaminas, String[] vitaminas
        Frutas pinia = new Frutas("pinia", 3, new String[]{"C", "B", "E"}, "fruta tropical");//String nombre, int nroVitaminas, String[] vitaminas, String tipo
        
        // guardar las frutas en un arreglo
        Frutas caja[] = {manzana, pera, pinia};
        
        // Veri1ficar cual fruta tiene mas vitaminas
        int mayorValue=0;
        String mayor="";
        for(Frutas f: caja){
            
            if(f.getnroVitaminas()>mayorValue){
                mayorValue = f.getnroVitaminas();
                mayor = f.getNombre();
            }
        }
        System.out.println("La fruta con mas vitaminas es: " + mayor);
        
        //  Mostrar las vitaminas de la fruta pera
        
        pera.mostrarVitaminas();
        
        // mostrar cantidad de vitaminas son citricas
        System.out.println("Cantidad de vitaminas citricas: " + pera.getnroVitaminasCitricas());
        
        // ordenar la frutas alfabeticamente segun el nombre de sus vitaminas
        manzana.ordenarVitaminas();
        pera.ordenarVitaminas();
        pinia.ordenarVitaminas();
        
        //ordenar las frutas segun el nombre de sus vitaminas
        
    }
}

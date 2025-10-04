package Ejercicio13;
import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author Joel Barrera Quispe Ejercicio13: 
 * a) Instanciar de 3 maneras diferentes 3 frutas con al menos 2 vitaminas cada una. 
 * b) Verificar cuál es la fruta con más vitaminas. 
 * c) Mostrar las vitaminas que tiene la fruta x. 
 * d) Cuantas vitaminas son cítricas. e) Ordenar las frutas alfabéticamente según el nombre de sus vitaminas.
 */
public class testFruta {

    public static void main(String[] args) {
        Frutas manzana = new Frutas();
        Frutas pera = new Frutas("pera", "fruta pomacea", 5, new String[]{"C", "A", "B", "K", "E"}); //String nombre, String tipo, int nroVitaminas, String[] vitaminas
        Frutas pinia = new Frutas("pinia", 3, new String[]{"C", "B", "E"}, "fruta tropical");//String nombre, int nroVitaminas, String[] vitaminas, String tipo
        
        System.out.println(manzana.toString());
        System.out.println(pera.toString());
        System.out.println(pinia.toString());
        
        // guardar las frutas en un arreglo
        List<Frutas> caja  = new ArrayList<>();
        caja.add(pinia);
        caja.add(pera);
        caja.add(manzana);
        
        // Veri1ficar cual fruta tiene mas vitaminas
        int mayorValue = 0;
        String mayor = "";
        for (Frutas f : caja) {

            if (f.getnroVitaminas() > mayorValue) {
                mayorValue = f.getnroVitaminas();
                mayor = f.getNombre();
            }
            
        }
        System.out.println("La fruta con mas vitaminas es: " + mayor);

        // mostrar cantidad de vitaminas son citricas
        System.out.println("numero de vitaminas citricas");
        for (Frutas e: caja){
            System.out.print(e.getNombre()+" ");
            System.out.println(e.getnroVitaminasCitricas());
        }

        // ordenar la frutas alfabeticamente segun el nombre de sus vitaminas
        manzana.ordenarVitaminas();
        pera.ordenarVitaminas();
        pinia.ordenarVitaminas();
        
        System.out.println("Lista de frutas desordenadas");
        for(Frutas g: caja){
            System.out.println(g.toString());
        }
        
        //ordenar las frutas segun el nombre de sus vitaminas
        for (int i = 0; i < caja.size(); i++) {
            int valori = (int) caja.get(i).getVitaminas()[0].charAt(0);
            for (int j = i+1; j < caja.size(); j++) {
                int valorj = (int) caja.get(j).getVitaminas()[0].charAt(0);
                if(valori>valorj){
                    Frutas temp = caja.get(i);
                    caja.set(i, caja.get(j));
                    caja.set(j, temp);
                }
            }
        }
        
        System.out.println("Lista de frutas ordenadas");
        for(Frutas g: caja){
            System.out.println(g.toString());
        }
    }
}

/**
 * Ejercicio 9. Sea la clase político(profesión, añosExp) y la clase Partido(nombreP,rol)
 * crear la clase presidente(nombre, apellido) que sea una clase hija de Político y Partido
 * a) Diseñar el diagrama de clases
 * b) Instanciar de dos formas diferentes a un presidente
 * c) Crear un vector de presidente con minimo 3 presidentes y buscar al presidente de
 * nombre x y mostrar el partido politico y la profesión.
 */
package Ejercicio_9;

/**
 *
 * @author Joel Barrera Quispe
 */
public class Sistema {
    public static void main(String[] args) {
        Presidente presi1 = new Presidente("Joel", "Barrera", "Naciones undas populares", "Dar bonos", "fisicoculturista", 36);
//        Presidente presi2 = new Presidente("Elva", "Tracio", "DAGP", "Partido politico", "informatico", 90);
        Presidente presi2 = new Presidente("informatico", 23,  "Elva", "Tracio", "DAGP");
        Presidente presi3 = new Presidente("Marco", "sito", "SON", "partido politico", "Cantante", 78);
        
        RegistroPresidentes R1 = new RegistroPresidentes();
        R1.agregarPresidente(presi1);
        R1.agregarPresidente(presi2);
        R1.agregarPresidente(presi3);
        System.out.println("Buscar a presidente Joel");
        R1.buscarPresidente("Joel");
    }
}

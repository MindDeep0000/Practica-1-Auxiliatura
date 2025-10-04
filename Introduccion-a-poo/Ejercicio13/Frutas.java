package Ejercicio13;

import java.util.Arrays;

/**
 * Ejercicio 13. Considere el siguiente diagrama de clases
 * 
 * nombre:kiwi 
 * tipo:subtropical 
 * nroVitaminas:3
 *
 * a) Instanciar de 3 maneras diferentes 3 frutas con al menos 2 vitaminas cada una. 
 * b) Verificar cuál es la fruta con más vitaminas. 
 * c) Mostrar las vitaminas que tiene la fruta x. 
 * d) Cuantas vitaminas son cítricas. 
 * e) Ordenar las frutas alfabéticamente según el nombre de sus vitaminas.
 */
public class Frutas {

    private String nombre, tipo;
    private int nroVitaminas;
    private String[] vitaminas;

    public Frutas() {
        this.nombre = "manzana";
        this.tipo = "fruta pomacea";
        this.nroVitaminas = 3;
        this.vitaminas = new String[]{"A", "C", "K"};
    }

    public Frutas(String nombre, String tipo, int nroVitaminas, String[] vitaminas) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = nroVitaminas;
        this.vitaminas = vitaminas;
    }

    public Frutas(String nombre, int nroVitaminas, String[] vitaminas, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = nroVitaminas;
        this.vitaminas = vitaminas;
    }

    public int getnroVitaminas() {
        return this.nroVitaminas;
    }

    public int getnroVitaminasCitricas() {
        int vitaminasCitricas = 0;
        for (int i = 0; i < this.vitaminas.length; i++) {
            if (this.vitaminas[i].equalsIgnoreCase("C")) {
                vitaminasCitricas++;
            }
        }
        return vitaminasCitricas;
    }

    public void ordenarVitaminas() {
        int valor1, valor2 = 0;
        String aux = "";
        for (int i = 0; i < this.vitaminas.length; i++) {
            for (int j = 0; j < this.vitaminas.length; j++) {
                valor1 = (int) vitaminas[i].toLowerCase().charAt(0);
                valor2 = (int) vitaminas[j].toLowerCase().charAt(0);

                if (valor1 < valor2) {
                    aux = vitaminas[i];
                    vitaminas[i] = vitaminas[j];
                    vitaminas[j] = aux;
                }
            }
        }
    }

    public String[] getVitaminas() {
        return vitaminas;
    }

    
    
    public String getNombre() {
        return this.nombre;
    }
    @Override
    public String toString(){
        return String.format("nombre: %s, tipo: %s, nroVitaminas: %d, vitaminas: %s", this.nombre, this.tipo, this.nroVitaminas, Arrays.toString(this.vitaminas));
    }
}

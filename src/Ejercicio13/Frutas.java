/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio13;

/**
 *
 * @author Joel Barrera Quispe
 * 
 */
public class Frutas {
    private String nombre, tipo;
    private int nroVitaminas;
    private String[] vitaminas;
    
    public Frutas(){
        this.nombre = "manzana";
        this.tipo = "fruta pomacea";
        this.nroVitaminas = 3;
        this.vitaminas = new String[]{"A", "C", "K"};
    }
    
    public Frutas(String nombre, String tipo, int nroVitaminas, String[] vitaminas){
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = nroVitaminas;
        this.vitaminas = vitaminas;
    }
    
    public Frutas(String nombre, int nroVitaminas, String[] vitaminas, String tipo){
        this.nombre = nombre;
        this.tipo = tipo;
        this.nroVitaminas = nroVitaminas;
        this.vitaminas = vitaminas;
    }
    
    public int getnroVitaminas(){
        return this.nroVitaminas;
    }
    
    public void mostrarVitaminas(){
        for(int i = 0; i<this.vitaminas.length; i++){
            System.out.print(vitaminas[i]+" ");
        }
        System.out.println("");
    }
    
    
    
    public int getnroVitaminasCitricas(){
        int vitaminasCitricas = 0;
        for(int i = 0; i<this.vitaminas.length; i++){
            if(this.vitaminas[i].equalsIgnoreCase("C")){
                vitaminasCitricas++;
            }
        }
        return vitaminasCitricas;
    }
    
    public void ordenarVitaminas(){
        int valor1, valor2 = 0;
        String aux="";
        for (int i = 0; i < this.vitaminas.length; i++) {
            for (int j = 0; j < this.vitaminas.length; j++) {
                valor1=(int) vitaminas[i].toLowerCase().charAt(0);
                valor2=(int) vitaminas[j].toLowerCase().charAt(0);
                
                if(valor1<valor2){
                    aux = vitaminas[i];
                    vitaminas[i] = vitaminas[j];
                    vitaminas[j] = aux;
                }
            }
        }
    }
    
    public String[] getVitaminas(){
        return vitaminas;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    
}

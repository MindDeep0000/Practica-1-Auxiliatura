package Ejercicio_11;
/**
 * Ejercicio 11. Dado la clase hija JefePolicia con las clases padres Persona, Empleado,
 * Policia. Se pide:
 * a) Identificar en cada clase 2 atributos significativos y crear 2 objetos de la clase hija
 * y mostrar sus datos.
 * b) Mostrar el nombre de aquel que tiene mayor sueldo.
 * c) Comparar si ambos tienen mismo grado
 * d) Implementar usando interfaces en java
 */


public class JefePolicia extends Persona implements iPersona, iEmpleado, iPolicia{
    private int sueldo;
    private String grado;
    private Empleado empleado;
    private Policia policia;
    
    
    public JefePolicia(String nombre, int edad, String ocupacion, int aniosExp, String especializacion, int aniosServicio, int sueldo, String grado){
        super(nombre, edad);
        this.empleado = new Empleado(ocupacion, aniosExp);
        this.policia = new Policia(especializacion, aniosServicio);
        this.sueldo = sueldo;
        this.grado = grado;
        
    }
    
    public String toString(){
        System.out.print(super.mostrarPersona());
        System.out.print(" "+this.mostrarEmpleado());
        System.out.print(" "+this.mostrarPolicia()+" ");
        return String.format("sueldo=%d grado=%s", this.sueldo, this.grado);
    }
    
    public int getSueldo(){
        return this.sueldo;
    }
    
    public String getGrado(){
        return this.grado;
    }
    
    public String comparaSueldo(JefePolicia otro){
        if(this.getSueldo()>otro.getSueldo()){
            return String.format("%s tiene mayor sueldo", this.getNombre());
        }
        return String.format("%s tiene mayor sueldo", otro.getNombre());
    }
    
    public boolean compararGrado(JefePolicia otro){
        if(this.getGrado().equals(otro.getGrado())){
            return true;
        }
        return false;
    }
    public String mostrarPolicia(){
        return String.format("especiaizacion=%s anios_de_servicio=%d", policia.getEspecializacion(), policia.getAniosServicio());
    }
    public String mostrarEmpleado(){
        
        return String.format("ocupacion=%s anios_de_experiencia=%d", empleado.getOcupacion(), empleado.getAniosExp());
    }
}

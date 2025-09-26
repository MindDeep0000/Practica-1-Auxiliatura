/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio5;

/**
 *
 * @author Joel Barrera Quispe inf 121 E
 * Aux. Cristian Alvarez
 */
public class Persona {
    private String nombre, paterno, materno;
    private int edad;
    private long ci;
    
    public Persona(String nombre, String paterno, String materno, int edad, int ci){
        this.nombre = nombre;
        this.paterno = paterno;
        this.materno = materno;
        this.edad = edad;
        this.ci = ci;
    }
    
    public String mostrarDatos(){
        return String.format("%s %s %s %d %d", this.nombre, this.paterno, this.materno, this.edad, this.ci);
    }
    
    public String mayorDeEdad(){
        if(this.edad>=18){
            return "es mayor de edad";
        }
        return "no es mayor de edad";
    }
    
    public void modificaredad(int nuevo){
        this.edad = nuevo;
    }
    
    public String tocayo(Persona nueva){
        if(this.paterno.equals(nueva.paterno)){
            return "Comparten el mismo apellido";
        }
        return "No comparten similitud en los apellidos";
    }
    
}

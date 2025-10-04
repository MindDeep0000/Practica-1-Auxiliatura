/**
 * Ejercicio 11. Dado la clase hija JefePolicia con las clases padres Persona, Empleado,
 * Policia. Se pide:
 * a) Identificar en cada clase 2 atributos significativos y crear 2 objetos de la clase hija
 * y mostrar sus datos.
 * b) Mostrar el nombre de aquel que tiene mayor sueldo.
 * c) Comparar si ambos tienen mismo grado
 * d) Implementar usando interfaces en java
 */
package Ejercicio_11;

public class Jefatura {

    public static void main(String[] args) {
        JefePolicia jf1 = new JefePolicia("Hugo", 34, "Policia", 23, "defensa", 40, 10000, "sargento");
        JefePolicia jf2 = new JefePolicia("Manuel", 56, "Militar", 40, "combate", 40, 20000, "suboficial");

        System.out.println(jf1.toString());
        System.out.println(jf2.toString());

        System.out.println(jf1.comparaSueldo(jf2));
        if (jf1.compararGrado(jf2)) {
            System.out.println("Mismo rango");
        } else {
            System.out.println("diferente rango");
        }
    }
}

package Ejercicio7;

/**
 *
 * Ejercicio 7. Dada la clase Mascota.
 *
 * a) Agrega un método para alimentar (+20 de energía, máximo 100). 
 * b) Agrega un método para jugar (-15 de energía, mínimo 0). 
 * c) Crea dos mascotas, aliméntalas y hazlas jugar, mostrando su energía en cada paso.
 */
public class TestMascota {

    public static void main(String[] args) {
        Mascota canino1 = new Mascota("Petardo", "pulgoso", 100);
        Mascota canino2 = new Mascota("Chamillo", "cachuchin", 80);

        System.out.println(canino1.estadoActual());
        System.out.println("alimentar +32 maximo: 100");
        canino1.alimentar(32, 100);
        System.out.println("jugar -50 minimo 30");
        canino1.jugar(50, 30);
        System.out.println(canino1.estadoActual());
        System.out.println("");

        System.out.println(canino2.estadoActual());
        System.out.println("alimentar +60 maximo 90");
        canino2.alimentar(60, 90);
        System.out.println("jugar -70 minimo 10");
        canino2.jugar(70, 10);
        System.out.println(canino2.estadoActual());
    }
}

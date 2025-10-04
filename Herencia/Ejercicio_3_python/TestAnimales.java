/**
 * Ejercicio 3. Crea una clase base Animal y subclases Leon, Pinguino, y Canguro. Agrega
 * un método desplazarse().
 * a) Crea la clase Animal con atributos nombre y edad, y el método desplazarse().
 * b) Cada subclase debe redefinir el método desplazarse() con su forma particular
 * (caminar, saltar, nadar).
 * c) Crea un arreglo de animales y haz que cada uno se desplace.
*/
package Ejercicio_3;

/**
 *
 * @author Joel Barrera Quispe
 */
public class TestAnimales {

    public static void main(String[] args) {

        Animal animales[] = {new Leon("Alex", 10), new Pinguino("Kriko", 5), new Canguro("Jack", 8)};

        for (Animal A : animales) {
            System.out.println(A.toString());
            A.desplazarse();
        }
    }
}

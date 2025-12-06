import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        ArchivoTrabajador archivo = new ArchivoTrabajador();
        try {
            archivo.crearArchivo();

            Trabajador t1 = new Trabajador("Ana", 1001, 1200.0);
            Trabajador t2 = new Trabajador("Luis", 1002, 1500.0);
            Trabajador t3 = new Trabajador("Maria", 1003, 1100.0);

            // Guardar una lista (sobrescribe)
            archivo.guardarTrabajadores(Arrays.asList(t1, t2, t3));

            // Guardar un trabajador adicional (append)
            Trabajador t4 = new Trabajador("Carlos", 1004, 1300.0);
            archivo.guardarTrabajador(t4);

            System.out.println("Lista inicial:");
            imprimirLista(archivo.leerTrabajadores());

            // Aumentar salario de Ana (carnet 1001)
            System.out.println("\nAumento de 200 a Ana...");
            archivo.aumentaSalario(200.0, t1);
            imprimirLista(archivo.leerTrabajadores());

            // Buscar mayor salario
            System.out.println("\nTrabajador con mayor salario:");
            Trabajador mayor = archivo.buscarMayorSalario();
            System.out.println(mayor != null ? mayor : "No hay trabajadores");

            // Ordenar por salario (desc)
            System.out.println("\nOrdenados por salario (desc):");
            List<Trabajador> ordenados = archivo.ordenarPorSalarioDesc();
            imprimirLista(ordenados);

        } catch (IOException e) {
            System.err.println("Error de E/S: " + e.getMessage());
        }
    }

    private static void imprimirLista(List<Trabajador> lista) {
        for (Trabajador t : lista)
            System.out.println(t);
    }
}

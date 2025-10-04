package Ejercicio15;

/**
 * 
 * Ejercicio 15.
 * 
 * a) Instanciar 3 buzones diferentes, cada uno con al menos 3 cartas. 
 * b) Instanciar 3 cartas con sus respectivas descripciones. 
 * c) Verificar cuántas cartas recibió el destinatario “X”. 
 * d) Eliminar la carta de la matriz cuyo código sea “X”. 
 * e) Verificar si algún remitente ha recibido alguna carta y,en ese caso, indicar de quién. 
 * f) Buscar una palabra clave (por ejemplo,"amor") en las descripciones de las cartas instanciadas. 
 * g) Por cada coincidencia, mostrar el código, remitente y destinatario correspondientes.
 */


import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class App {

    public static void main(String[] args) {
        
        System.out.println("Operaciones en buzon1: ");

        Carta c1 = new Carta("c456", "Querido amigo te escribo para decirte que ella note ama");
        Carta c2 = new Carta("c123", "Quieres venir a jugar a mi casa el lunes?");
        Carta c3 = new Carta("c789", "Dile a wilmer que ya no me busque mas");

        Carta[] cartas = {c1, c2, c3};

        List<List<String>> matriz = new ArrayList<>();
        
        matriz.add(new ArrayList<>(Arrays.asList("c123", "Juan Alvarez", "Peter Chavez")));
        matriz.add(new ArrayList<>(Arrays.asList("c456", "Pepe Mujica", "Wilmer perez")));
        matriz.add(new ArrayList<>(Arrays.asList("c789", "Paty Vazques", "Pepe Mujica")));

        Buzon buzon1 = new Buzon(001, 3, matriz);

        System.out.println(buzon1.getnroCartasDeDestinatario("Wilmer perez"));

        buzon1.mostrarBuzon();
        buzon1.eliminarCarta("c123");
        buzon1.mostrarBuzon();

        buzon1.cartaAremitente();
        if (c1.buscarPalabra("ama")) {
            buzon1.buscarCarta(c1.getCodigo());
        }
        
        
        
        System.out.println("\nOperaciones en buzon2: ");
        
        Carta c4 = new Carta("c001", "Hola quieres salir a comer algo?");
        Carta c5 = new Carta("c002", "hi mr president, i love America. Don't kick me out of America");
        Carta c6 = new Carta("c003", "hi. Donald!! Quieles il a jugal con misiles en la talde? Putin ya se apunto. Que hadlas tu?");

        Carta[] cartas2 = {c4, c5, c6};
        
        List<List<String>> matriz2 = new ArrayList<>();
        matriz2.add(new ArrayList<>(Arrays.asList("c001", "Donald Trump", "Ramy Maguel")));
        matriz2.add(new ArrayList<>(Arrays.asList("c002", "Pablo Osco", "Donald Trump")));
        matriz2.add(new ArrayList<>(Arrays.asList("c003", "Xi Ji Ping", "Donald Trump")));
        
        Buzon buzon2 = new Buzon(002, 3, matriz2);
        
        System.out.println(buzon2.getnroCartasDeDestinatario("Donald Trump"));

        buzon2.mostrarBuzon();
        buzon2.eliminarCarta("c002");
        buzon2.mostrarBuzon();
        System.out.print("Cartas a remitentes");
        buzon2.cartaAremitente();
        
        if (c6.buscarPalabra("misiles")) {
            buzon2.buscarCarta(c6.getCodigo());
        }
        
        
        System.out.println("\nOperaciones en buzon3: ");
        
        Carta c7 = new Carta("c004", "Llego pedro a su casa el viernes por la noche?");
        Carta c8 = new Carta("c005", "Haz visitado la plaza del pueblo? Deberiamos ir tienes estatuas interesantes.");
        Carta c9 = new Carta("c006", "Si llego muy tarde el esta enfermo te hablara cuando este bien.");

        Carta[] cartas3 = {c7, c8, c9};
        
        List<List<String>> matriz3 = new ArrayList<>();
        matriz3.add(new ArrayList<>(Arrays.asList("c004", "Paco Fuentes", "Jhon Bueno")));
        matriz3.add(new ArrayList<>(Arrays.asList("c005", "Pedro Vazquez", "Paco Fuentes")));
        matriz3.add(new ArrayList<>(Arrays.asList("c006", "Jhon bueno", "Paco Fuentes")));
        
        Buzon buzon3 = new Buzon(003, 3, matriz3);
        
        System.out.println(buzon3.getnroCartasDeDestinatario("Pedro Vasquez"));

        buzon3.mostrarBuzon();
        buzon3.eliminarCarta("c005");
        buzon3.mostrarBuzon();
        System.out.print("Cartas a remitentes");
        buzon3.cartaAremitente();
        
        if (c9.buscarPalabra("enfermo")) {
            buzon3.buscarCarta(c9.getCodigo());
        }

    }
}

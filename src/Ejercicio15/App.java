/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicio15;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

/**
 *
 * @author ACCESO
 */
public class App {
    public static void main(String[] args) {
        
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
        if(c1.buscarPalabra("ama")){
            buzon1.buscarCarta(c1.getCodigo());
        }
//        
//        
//        Buzon buzon2 = new Buzon(002, 2, new String[][]{ {"c123", "Juan Alvarez", "Peter Chavez"}, 
//                                                         {"c456", "Pepe Mujica", "Wilmer perez" }, 
//                                                         {"c789", "Paty Vazques", "Pepe Mujica" } });
        
        
    }
}

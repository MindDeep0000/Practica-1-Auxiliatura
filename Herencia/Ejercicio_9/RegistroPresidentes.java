package Ejercicio_9;

import java.util.ArrayList;
/**
 *
 * @author ACCESO
 */
public class RegistroPresidentes {
    ArrayList<Presidente> registro = new ArrayList<>();
    public RegistroPresidentes(){}
    public void agregarPresidente(Presidente p){
        registro.add(p);
    }
    public void buscarPresidente(String nombre){
        for(Presidente p : registro){
            if(p.getNombre().equals(nombre)){
                System.out.println(p.toString());
                break;
            }
        }
    }
    
    
}

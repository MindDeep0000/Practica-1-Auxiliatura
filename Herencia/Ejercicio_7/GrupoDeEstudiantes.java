package Ejercicio_7;
import java.util.ArrayList;
/**
 *
 * @author ACCESO
 */
public class GrupoDeEstudiantes {
    ArrayList<Estudiante> edades = new ArrayList<>();
    public GrupoDeEstudiantes() {
        
    }
    
    public void agregarEstudiante(Estudiante est){
        edades.add(est);
    }

    public double promedio() {
        int suma = 0;
        for (Estudiante p: edades){
            suma += p.getEdad();
        }
        return suma / edades.size();
    }
}

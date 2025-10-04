package Ejercicio_13;
import java.util.ArrayList;
import java.util.List;
public class Empleado {
    private String nombre;
    private int sueldoMes;
    private List<Empleado> lista;

    public Empleado() {
        lista = new ArrayList<>();
    }

    public Empleado(String nombre, int sueldoMes) {
        this.nombre = nombre;
        this.sueldoMes = sueldoMes;
    }
    
    public void aniadir(Empleado a){
        lista.add(a);
    }
    
    public void mostrarSueldo(int sueldoMes){
        
        for(Empleado E: lista){
            if(E.getSueldoMes()==sueldoMes){
                System.out.println(E.toString());
            }
        }
    }
    
    public double sueldoTotal(){
        double total=0;
        for(Empleado e: lista){
            if(e instanceof Chef){
                Chef c1 = (Chef)e;
                total+=c1.sueldoTotal(0);
                total+=c1.getSueldoMes();
                
            }
            if(e instanceof Mesero){
                Mesero m1 = (Mesero) e;
                total+=m1.getPropina();
                total+=m1.getSueldoMes();
            }
            
            if(e instanceof Administrativo){
                total+=e.getSueldoMes();
            }
        }
        
        return total;
    }

    public String getNombre() {
        return nombre;
    }

    public int getSueldoMes() {
        return sueldoMes;
    }

    @Override
    public String toString() {
        return "Empleado{" + "nombre="+ nombre+" sueldoMes=" + sueldoMes + '}';
    }
    
}

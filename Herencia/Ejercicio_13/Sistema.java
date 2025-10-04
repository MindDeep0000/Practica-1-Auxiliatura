package Ejercicio_13;

/**
 *
 * @author ACCESO
 */
public class Sistema {
    public static void main(String[] args) {
        
        Empleado e = new Empleado();
        
        
        Chef c = new Chef(5, "chef de partida", 200, "Ausguto", 12000);
        e.aniadir(c);
        
        Administrativo a = new Administrativo("tramites administrativos", "Joel", 6000);
        Administrativo b = new Administrativo("manejo de bases de datos", "Benjamin", 8000);
        e.aniadir(a);
        e.aniadir(b);
        
        
        Mesero m1 = new Mesero(3, 5, 10, "Ben", 3000);
        Mesero m2 = new Mesero(5, 3, 15, "Fred", 3000);
        e.aniadir(m1);
        e.aniadir(m2);
        
        System.out.println("Empleado que ganan 3000");
        e.mostrarSueldo(3000);
        
        System.out.println("Suma total de los sueldos de todos los Empleados");
        System.out.println(e.sueldoTotal());
        
    }
}

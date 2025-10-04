package Ejercicio_9;


public class Presidente extends Politico {

    private String nombre, apellido;
    private Partido p1;
    private Partido p2;

    public String getNombre() {
        return nombre;
    }

    public Presidente(String nombre, String apellido, String nombreP, String rol, String profesion, int aniosExp) {
        super(profesion, aniosExp);
        this.nombre = nombre;
        this.apellido = apellido;
        p1 = new Partido(nombreP, rol);
    }

    public Presidente(String profesion, int aniosExp, String nombre, String apellido, String nombreP) {
        super(profesion, aniosExp);
        this.nombre = nombre;
        this.apellido = apellido;
        p2 = new Partido(nombreP);
    }

    @Override
    public String toString() {
        return String.format("nombre: %s, profesion: %s", this.nombre, super.getProfesion());
    }

}

public class Doctor {
    private String nombre;
    private String especialidad;

    public Doctor(String nom, String esp) {
        this.nombre = nom;
        this.especialidad = esp;
    }

    @Override
    public String toString() {
        return "nombre: " + this.nombre + " esp: " + this.especialidad;
    }
}

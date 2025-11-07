import java.util.ArrayList;
import java.util.List;

class Hospital {
    private String nombre;
    private List<Doctor> doctores;

    public Hospital(String nombre) {
        this.nombre = nombre;
        this.doctores = new ArrayList<>();
    }

    public void agregarDoctor(Doctor dr) {
        doctores.add(dr);
    }

    public void mostrarDoctores() {
        System.out.println("*** " + nombre + "\n<<doctores>>");
        for (Doctor d : doctores) {
            System.out.println(d);
        }
    }
}

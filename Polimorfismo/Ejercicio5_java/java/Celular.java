package Polimorfismo.Ejercicio5.python;

public class Celular {
    private int numeroDeTelefono;
    private String dueño;
    private double espacio;
    private double ram;
    private int numeroApp;

    public Celular(int numeroDeTelefono, String dueño, double espacio, double ram, int numeroApp) {
        this.numeroDeTelefono = numeroDeTelefono;
        this.dueño = dueño;
        this.espacio = espacio;
        this.ram = ram;
        this.numeroApp = numeroApp;
    }

    public void iadd() {
        this.numeroApp += 10;
    }

    public void dsub() {
        this.espacio -= 5;
        this.espacio = Math.round(this.espacio * 100.0) / 100.0; // rounding to 2 decimal places
    }

    @Override
    public String toString() {
        return "nro: " + this.numeroDeTelefono + " - dueño: " + this.dueño + " - espacio: " + this.espacio + " GB - ram: " + this.ram + " GB - nroApps: " + this.numeroApp;
    }

    public static void main(String[] args) {
        Celular celular = new Celular(78929330, "Joel", 6.44, 10, 20);
        System.out.println(celular.toString());
        celular.iadd();
        celular.dsub();
        System.out.println(celular.toString());
    }
}
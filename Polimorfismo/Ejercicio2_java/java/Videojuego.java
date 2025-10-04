package Polimorfismo.Ejercicio2.python;

class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidadDeJugadores;

    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadDeJugadores = 0;
    }

    public Videojuego(String nombre, int cantidadDeJugadores) {
        this.nombre = nombre;
        this.plataforma = null;
        this.cantidadDeJugadores = cantidadDeJugadores;
    }

    public Videojuego(String nombre, String plataforma, int cantidadDeJugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadDeJugadores = cantidadDeJugadores;
    }

    public void agregarJugadores() {
        this.cantidadDeJugadores += 1;
    }

    public void agregarJugadores(int variosJugadores) {
        this.cantidadDeJugadores += variosJugadores;
    }

    @Override
    public String toString() {
        return "Nombre: " + this.nombre + " plataforma: " + this.plataforma + " cantidad de jugadores: " + this.cantidadDeJugadores;
    }

    public static void main(String[] args) {
        Videojuego borderlands = new Videojuego("Borderlands", "steam");
        Videojuego wow = new Videojuego("World of warcraft", "Steam", 100000);

        System.out.println(borderlands.toString());
        System.out.println(wow.toString());
        borderlands.agregarJugadores(4);
        wow.agregarJugadores(200);
        System.out.println(borderlands.toString());
        System.out.println(wow.toString());
    }
}


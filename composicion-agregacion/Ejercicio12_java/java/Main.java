public class Main {
    public static void main(String[] args) {
        Hospital hospital1 = new Hospital("Hospital de la sierra");
        Hospital hospital2 = new Hospital("Hospital de villa tunari");

        Doctor doctor1 = new Doctor("Dr. Antonio Berruezo Sánchez", "Arritmias Cardíacas");
        Doctor doctor2 = new Doctor("Pedro Cavadas", "cirujano plástico y referente en trasplantes de manos");
        Doctor doctor3 = new Doctor("Dr. César Canales Bedoya", "cirugías de tiroides y biliopancreáticas");
        Doctor doctor4 = new Doctor("Dr. Gonzalo Aldámiz-Echevarría del Castillo", "jefe de Cirugía Cardíaca");
        Doctor doctor5 = new Doctor("Dra. Manuela Camino López", "líder en Trasplante Cardíaco Infantil");

        hospital1.agregarDoctor(doctor1);
        hospital1.agregarDoctor(doctor2);

        hospital2.agregarDoctor(doctor3);
        hospital2.agregarDoctor(doctor4);
        hospital2.agregarDoctor(doctor5);

        hospital1.mostrarDoctores();
        hospital2.mostrarDoctores();
    }
}

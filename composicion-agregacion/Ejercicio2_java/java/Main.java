public class Main {
    public static void main(String[] args) {
        Empleado employee1 = new Empleado("Jose", "Administrador", 12000);
        Empleado employee2 = new Empleado("Abel", "Sistemas", 10000);
        Empleado employee3 = new Empleado("Marco", "Tecnico supervisor", 14000);
        Empleado employee4 = new Empleado("Rafa", "vendedor", 5000);
        Empleado employee5 = new Empleado("Araceli", "vendedora", 4000);

        Departamento department1 = new Departamento("Ventas", "area de ventas");
        department1.aniadir(employee1);
        department1.aniadir(employee2);
        department1.aniadir(employee3);

        Departamento department2 = new Departamento("plaza 1", "sistemas");
        department2.aniadir(employee1);
        department2.aniadir(employee4);
        department2.aniadir(employee5);

        System.out.println("mostrar empleados\n-------------------------------------------------------");
        System.out.println("departamento 1");
        department1.mostrarEmpleados();
        System.out.println("departamento 2");
        department2.mostrarEmpleados();
        System.out.println("-------------------------------------------------------");
        System.out.println("cambiar salario\n-------------------------------------------------------");
        department1.cambioSalario("Marco", 15000);
        department2.cambioSalario("Jose", 1000);
        System.out.println("-------------------------------------------------------");
        System.out.println("verificar si son del mismo departamento\n-------------------------------------------------------");
        department1.verificarMismoDepartamento(department2);
        System.out.println("-------------------------------------------------------");
        System.out.println("mover empleados a departamento nuevo\n-------------------------------------------------------");
        department1.cambiarDepartamento(department2);
        System.out.println("departamento 1");
        department1.mostrarEmpleados();
        System.out.println("departamento 2");
        department2.mostrarEmpleados();
        System.out.println("-------------------------------------------------------");
    }
}
